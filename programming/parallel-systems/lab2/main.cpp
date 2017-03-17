#include <iostream>
#include <windows.h>
#include <process.h>
#include <cmath>
#include <cstdlib>
#include <chrono>

#define CHECK(condition) if (!condition) std::cerr

using namespace std;
double *pi;
int n;
int threads_num;

unsigned int WINAPI ThreadFunction(void *param) {
    int index = (int) param;
    double h = 1.0 / n;
    double sum = 0.0;

    for (int i = index; i < n; i += threads_num) {
        double x;
        x = h * i;
        sum += 4. / (1. + x * x);
    }
    pi[index] = h * sum;
    return 0;
}

double count_pi() {
    cout << "calculate pi with " << threads_num << " threads and n=" << n << endl;
    pi = new double[threads_num];
    LARGE_INTEGER freq, hq_start_time, hq_end_time;
    HANDLE *hThreads = new HANDLE[threads_num];

    auto win_start_time = GetTickCount();
    auto cpp11_start_time = std::chrono::steady_clock::now();
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&hq_start_time);

    // create child threads
    for (int i = 0; i < threads_num; i++) {
        hThreads[i] = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction, (void *) i, 0, NULL);
        // error handling
        CHECK(hThreads[i]) << "Create Thread Error: " << GetLastError() << endl;
    }

    // wait for child threads terminating
    WaitForMultipleObjects(threads_num, hThreads, TRUE, INFINITE);
    cout << "Child threads terminate successfully" << endl;

    // close threads objects
    for (int i = 0; i < threads_num; i++) {
        CloseHandle(hThreads[i]);
    }

    double sum = 0.0;
    for (int i = 0; i < threads_num; i++) {
        sum += pi[i];
    }

    // calculate time
    auto win_elapsed = GetTickCount() - win_start_time;
    auto cpp11_end_time = std::chrono::steady_clock::now();
    auto cpp11_elapsed =
            std::chrono::duration_cast<std::chrono::nanoseconds>(cpp11_end_time - cpp11_start_time).count() / 1000000;
    QueryPerformanceCounter(&hq_end_time);
    double hq_elapsed = 1000. * (hq_end_time.QuadPart - hq_start_time.QuadPart) / freq.QuadPart;

    cout << "pi=" << sum << endl;
    cout << "GetTickCount time=" << win_elapsed << " ms" << endl;
    cout << "cpp1 time=" << cpp11_elapsed << " ms" << endl;
    cout << "QueryPerformance time=" << hq_elapsed << " ms" << endl;
    return sum;
}

int main(int argc, char *argv[]) {
    int dims[4] = {100000, 1000000, 10000000, 100000000};

    for (int i = 0; i < 4; i++) {
        n = dims[i];
        for (int j = 1; j < 5; j++) {
            threads_num = j;
            count_pi();
        }
    }
    
    return 0;
}