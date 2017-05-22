//
// Created by Drapegnik on 21.05.17.
//
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <winsock2.h>
#include <iphlpapi.h>
#include <stdio.h>
#include <iostream>

using namespace std;

void handle_error(DWORD error);

int main(int argc, char **argv) {
    DWORD return_value;
    IPAddr dest_ip = 0;
    IPAddr src_ip = 0;       //  default for src ip
    ULONG mac_address[2];       //  for 6-byte hardware addresses
    ULONG address_len = 6;  //  default to length of six bytes
    BYTE *address;

    char *dest_ip_str = argv[1];
    if (dest_ip_str == NULL) {
        cerr << "Destination IP is required! Pass it as command line argument" << endl;
        return 1;
    }
    dest_ip = inet_addr(dest_ip_str);
    cout << "Sending ARP request";

    char *src_ip_str = argv[2];
    if (src_ip_str != NULL) {
        src_ip = inet_addr(src_ip_str);
        cout << " from " << src_ip_str;
    }
    cout << " to " << dest_ip_str << endl;

    return_value = SendARP(dest_ip, src_ip, mac_address, &address_len);

    if (return_value != NO_ERROR) {
        handle_error(return_value);
        return 1;
    }

    address = (BYTE *) &mac_address;
    if (!address_len) {
        cerr << "SendArp completed successfully, but returned length=0" << endl;
        return 1;
    }

    cout << "Mac address: ";
    for (int i = 0; i < (int) address_len; i++) {
        printf("%.2X", (int) address[i]);
        if (i == (address_len - 1)) {
            cout << endl;
            break;
        }
        cout << "-";
    }

    return 0;
}

void handle_error(DWORD error) {
    cerr << "SendArp failed with error: " << error;
    switch (error) {
        case ERROR_GEN_FAILURE:
            cerr << " (ERROR_GEN_FAILURE)" << endl;
            break;
        case ERROR_INVALID_PARAMETER:
            cerr << " (ERROR_INVALID_PARAMETER)" << endl;
            break;
        case ERROR_INVALID_USER_BUFFER:
            cerr << " (ERROR_INVALID_USER_BUFFER)" << endl;
            break;
        case ERROR_BAD_NET_NAME:
            cerr << " (ERROR_BAD_NET_NAME)" << endl;
            break;
        case ERROR_BUFFER_OVERFLOW:
            cerr << " (ERROR_BUFFER_OVERFLOW)" << endl;
            break;
        case ERROR_NOT_FOUND:
            cerr << " (ERROR_NOT_FOUND)" << endl;
            break;
        default:
            cerr << endl;
            break;
    }
}
