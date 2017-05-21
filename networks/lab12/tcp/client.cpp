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
    char buffer[128];
    char server_name[20];
    int ret_val;
    unsigned int address;
    struct sockaddr_in server;
    struct hostent *hp;
    WSADATA wsaData;
    SOCKET conn_socket;

    if (WSAStartup(0x101, &wsaData) == SOCKET_ERROR) {
        cerr << "[client]: WSAStartup failed with error " << WSAGetLastError() << endl;
        WSACleanup();
        return -1;
    }

    cout << "[client]: Input server IP-address: ";
    cin >> server_name;

    if (isalpha(server_name[0])) {
        hp = gethostbyname(server_name);    // server address is a name
    } else {
        address = inet_addr(server_name);   //  convert nnn.nnn address to a usable one
        hp = gethostbyaddr((char *) &address, 4, AF_INET);
    }
    if (hp == NULL) {
        cerr << "[client]: cannot resolve address [" << server_name << "]: error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }

    //  create a socket
    conn_socket = socket(AF_INET, socket_type, 0);
    if (conn_socket == INVALID_SOCKET) {
        cerr << "[client]: Error Opening socket: error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }

    //  copy into the sockaddr_in structure
    memset(&server, 0, sizeof(server));
    memcpy(&(server.sin_addr), hp->h_addr, hp->h_length);
    server.sin_family = hp->h_addrtype;
    server.sin_port = htons(port);

    cout << "[client]: connecting to: " << hp->h_name << endl;
    if (connect(conn_socket, (struct sockaddr *) &server, sizeof(server)) == SOCKET_ERROR) {
        cerr << "[client]: connect() failed: " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }

    cout << "[client]: Input message: ";
    cin >> buffer;

    ret_val = send(conn_socket, buffer, sizeof(buffer), 0);
    if (ret_val == SOCKET_ERROR) {
        cerr << "[client]: send() failed: error " << WSAGetLastError() << endl;
        WSACleanup();
        return 1;
    }
    cout << "[client]: sent data [" << buffer << "]" << endl;

    ret_val = recv(conn_socket, buffer, sizeof(buffer), 0);
    if (ret_val == SOCKET_ERROR) {
        cerr << "[client]: recv() failed: error " << WSAGetLastError() << endl;
        closesocket(conn_socket);
        WSACleanup();
        return 1;
    }

    if (ret_val == 0) {
        cout << "[client]: server closed connection" << endl;
        closesocket(conn_socket);
        WSACleanup();
        return 1;
    }
    cout << "[client]: received " << ret_val << " bytes, data [" << buffer << "] from server" << endl;

    char c;
    cout << "[client]: type any key to disconnect" << endl;
    cin >> c;
    closesocket(conn_socket);
    WSACleanup();
    return 0;
}
