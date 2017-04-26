#include <windows.h>
#include <process.h>
#include <iostream>
#include "Car.h"
#include "Garage.h"

#define CHECK(condition) if (!condition) std::cerr

using namespace std;

bool bTerminate = false;
CRITICAL_SECTION cs;
HANDLE hSemaphore;
Garage garage;

unsigned int WINAPI ThreadFunction(void *param) {
    int index = (int) param;
    Car car = Car(index);
    while (!bTerminate) {
        if (car.isInGarage()) {
            Sleep(rand() % 10000);
            EnterCriticalSection(&cs);
            car.leaveGarage();
            garage.freePlace();
            LeaveCriticalSection(&cs);
            ReleaseSemaphore(hSemaphore, 1, NULL);
        } else {
            Sleep(rand() % 10000);
            WaitForSingleObject(hSemaphore, INFINITE);
            EnterCriticalSection(&cs);
            car.enterGarage();
            garage.takePlace();
            LeaveCriticalSection(&cs);
        }
        cout << "--------------------------------------" << endl;
    }

    if (car.isInGarage()) {
        EnterCriticalSection(&cs);
        car.leaveGarage();
        garage.freePlace();
        LeaveCriticalSection(&cs);
        ReleaseSemaphore(hSemaphore, 1, NULL);
    }

    EnterCriticalSection(&cs);
    car.getInfo();
    cout << "--------------------------------------" << endl;
    LeaveCriticalSection(&cs);
    return 0;
}

int main(int argc, char *argv[]) {
    garage = Garage(atoi(argv[1]));   // garage size
    int cars_num = atoi(argv[2]);     // number of threads

    cout << "(main): There are " << garage.getSize() << " places and " << cars_num << " cars." << endl;
    cout << "(main): Start race! Type any key terminating:" << endl;
    cout << "--------------------------------------" << endl;

    HANDLE hThreads[cars_num];
    InitializeCriticalSection(&cs);
    hSemaphore = CreateSemaphore(NULL,  garage.getSize(), garage.getSize(), NULL);
    CHECK(hSemaphore) << "(main): Create Semaphore Error: " << GetLastError() << std::endl;

    for (int i = 0; i < cars_num; i++) {
        // create child thread (car) and passing index param
        hThreads[i] = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction, (void *) i, 0, NULL);
        // error handling
        CHECK(hThreads[i]) << "(main): Create Thread Error: " << GetLastError() << endl;
    }

    string promt;
    cin >> promt;
    bTerminate = true;

    WaitForMultipleObjects(cars_num, hThreads, TRUE, INFINITE);
    cout << "(main): All child threads terminate successfully!" << endl;
    garage.getStatus();
    return 0;
}