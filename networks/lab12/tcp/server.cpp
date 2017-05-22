//
// Created by Drapegnik on 21.05.17.
//
#include <winsock.h>
#include <stdio.h>
#include <iostream>

#define DEFAULT_PORT 5001

using namespace std;

int main(void) {
    int socket_type = SOCK_STREAM;   // TCP-protocol
    unsigned short port = DEFAULT_PORT;
    WSADATA wsaData;
    SOCKET listen_socket, msg_sock;
    char buffer[128];
    int ret_val;
    int from_len;
    struct sockaddr_in local, from;

    if (WSAStartup(0x101, &wsaData) == SOCKET_ERROR) {
        cerr << "[server]: WSAStartup failed with error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }

    //  create a socket
    listen_socket = socket(AF_INET, socket_type, 0); // TCP socket
    if (listen_socket == INVALID_SOCKET) {
        cerr << "[server]: Error Opening socket: error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }

    //  bind() associates a local address and port combination with the
    //  socket just created.
    local.sin_family = AF_INET;
    local.sin_addr.s_addr = INADDR_ANY;
    local.sin_port = htons(port);  //   port must be in Network Byte Order

    if (bind(listen_socket, (struct sockaddr *) &local, sizeof(local)) == SOCKET_ERROR) {
        cerr << "[server]: bind() failed with error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }

    if (listen(listen_socket, 5) == SOCKET_ERROR) {
        cerr << "[server]: listen() failed with error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }
    cout << "[server]: listening port " << port << ", protocol TCP" << endl;

    from_len = sizeof(from);

    msg_sock = accept(listen_socket, (struct sockaddr *) &from, &from_len);
    if (msg_sock == INVALID_SOCKET) {
        cerr << "[server]: accept() error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }
    cout << "[server]: new connection from " << inet_ntoa(from.sin_addr) << ", port " << htons(from.sin_port) << endl;

    ret_val = recv(msg_sock, buffer, sizeof(buffer), 0);
    if (ret_val == SOCKET_ERROR) {
        cerr << "[server]: recv() failed: error " << WSAGetLastError() << endl;
        closesocket(msg_sock);
        return 1;
    }
    if (ret_val == 0) {
        cout << "[server]: client closed connection" << endl;
        closesocket(msg_sock);
        return 1;
    }
    cout << "[server]: received " << ret_val << " bytes, data [" << buffer << "] from client" << endl;

    cout << "[server]: Input message: ";
    cin >> buffer;

    ret_val = send(msg_sock, buffer, sizeof(buffer), 0);
    if (ret_val == SOCKET_ERROR) {
        cerr << "[server]: send() failed: error " << WSAGetLastError() << endl;
    }

    char c;
    cout << "[server]: press any key to disconnect" << endl;
    cin >> c;
    closesocket(msg_sock);
    WSACleanup();
    return 0;
}
