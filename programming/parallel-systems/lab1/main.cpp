#include <iostream>
#include <windows.h>
#include <process.h>
#include <stdio.h>
#include <cmath>

using namespace std;
bool bTerminate = false;

struct Params {
    int k;
    double x;
};

unsigned int WINAPI ThreadFunction(void *pvParams) {
    Params *params = (Params *) pvParams;
    cout << "(child): calculate function sin(" << params->x << ")" << endl;
    int i = 0;
    double sum;
    while (!bTerminate) {
        sum = sin(params->x);
        i++;
        if (i == params->k) {
            break;
        }
    }
    cout << "(child): terminating after " << i << " iterations" << endl;
    cout << "(child): sin(" << params->x << ") = " << sum << endl;
    return 0;
}

double sinx(double x) {
    double n = x;
    double sum = 0.0;
    int i = 1;

    do {
        sum += n;
        n *= -1.0 * x * x / ((2 * i) * (2 * i + 1));
        i++;
    } while (fabs(n) > 0.000000001);

    return sum;
}

int main(int argc, char *argv[]) {
    Params params = Params();
    params.x = atof(argv[1]);
    cout << "(main): Do you want terminate thread by action or after k iterations? (0/k)" << endl;
    cin >> params.k;
    if (params.k == 0) {
        cout << "(main): Type anything for terminating thread" << endl;
    }

    // create child thread and passing params
    HANDLE hThread = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction, (void *) &params, 0, NULL);
    string promt;
    if (params.k == 0) {
        cin >> promt;
        bTerminate = true;
    }

    // error handling
    if (hThread == NULL) {
        printf("Create Thread Error=%d\n", GetLastError());
        return -1;
    }

    // wait for child thread terminating
    WaitForSingleObject(hThread, INFINITE);
    cout<<"(main): Child thread terminate successfully";

    // close thread object
    CloseHandle(hThread);
    return 0;
}