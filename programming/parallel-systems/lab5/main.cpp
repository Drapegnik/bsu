#include <iostream>
#include <fstream>
#include <windows.h>
#include <process.h>

#define CHECK(condition) if (!condition) std::cerr

using namespace std;
FILE *file = fopen("report.tex", "w");
CRITICAL_SECTION cs;
int **matrix;
int *vector, *result;
int n, threads_num, current_row;
double one_time;

int **initMatrix(int n);

unsigned int WINAPI ThreadFunction1(void *param) {
    int i = int(param);
    int sum = 0;
    for (int j = 0; j < n; j++) {
        sum += matrix[i][j] * vector[j];
    }
    result[i] = sum;
    return 0;
}

unsigned int WINAPI ThreadFunction2(void *param) {
    int i;
    while (true) {
        EnterCriticalSection(&cs);
        if (current_row >= n) {
            LeaveCriticalSection(&cs);
            break;
        }

        i = current_row;
        current_row++;
        int sum = 0;
        for (int j = 0; j < n; j++) {
            sum += matrix[i][j] * vector[j];
        }
        result[i] = sum;
        LeaveCriticalSection(&cs);
    }
    return 0;
}

void multiply1() {
    cout << "-----------------------------------" << endl;
    cout << "multiply1:" << endl;
    cout << "n=" << n << " with " << n << " threads: ";
    HANDLE *hThreads = new HANDLE[n];
    LARGE_INTEGER freq, start_time, end_time;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&start_time);

    // create child threads
    for (int i = 0; i < n; i++) {
        hThreads[i] = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction1, (void *) i, 0, NULL);
        // error handling
        // CHECK(hThreads[i]) << "Create Thread Error: " << GetLastError() << endl;
    }

    // wait for child threads terminating
    WaitForMultipleObjects(n, hThreads, TRUE, INFINITE);

    // close threads objects
    for (int i = 0; i < n; i++) {
        CloseHandle(hThreads[i]);
    }

    QueryPerformanceCounter(&end_time);
    double elapsed = 1000. * (end_time.QuadPart - start_time.QuadPart) / freq.QuadPart;
    cout << elapsed << " ms" << endl;

    fprintf(file, " & %.3f ms", elapsed);
    cout << "-----------------------------------" << endl;

    delete[] hThreads;
    return;
}

void multiply2() {
    cout << "n=" << n << " with " << threads_num << " threads: ";
    HANDLE *hThreads = new HANDLE[threads_num];
    LARGE_INTEGER freq, start_time, end_time;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&start_time);

    // create child threads
    for (int i = 0; i < threads_num; i++) {
        hThreads[i] = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction2, (void *) i, 0, NULL);
        // error handling
        CHECK(hThreads[i]) << "Create Thread Error: " << GetLastError() << endl;
    }

    // wait for child threads terminating
    WaitForMultipleObjects(threads_num, hThreads, TRUE, INFINITE);

    // close threads objects
    for (int i = 0; i < threads_num; i++) {
        CloseHandle(hThreads[i]);
    }

    QueryPerformanceCounter(&end_time);
    double elapsed = 1000. * (end_time.QuadPart - start_time.QuadPart) / freq.QuadPart;
    cout << elapsed << " ms" << endl;

    if (threads_num == 1) { one_time = elapsed; }

    double acc = one_time / elapsed;
    fprintf(file, " & %.3f & %.3f & %.3f", elapsed, acc, acc / threads_num);
    delete[] hThreads;
    return;
}

void print_table_header(int threads) {
    fprintf(file, "\\begin{tabular}{|");
    for (int i = 0; i < 6; i++) {
        fprintf(file, "l|");
    }
    fprintf(file, "}\\hline\n");
    fprintf(file, "\\multicolumn{1}{|c|}{\\textbf{dimensions}} &");
    fprintf(file, "\\multicolumn{1}{|c|}{\\textbf{model 1}} &");
    fprintf(file, "\\multicolumn{3}{|c|}{\\textbf{model 2}}");
    fprintf(file, "\\\\ \\hline\n");
    fprintf(file, "& & \\multicolumn{3}{c|}{\\textbf{%d Thread%s}} ", threads, threads == 1 ? "" : "s");
    fprintf(file, "\\\\ \\hline\n");
    fprintf(file, "& \\textbf{time} & \\textbf{time} & \\textbf{acc} & \\textbf{eff}");
    fprintf(file, "\\\\ \\hline\n");
    return;
}

int *initVector(int n) {
    int *temp = new int[n];
    for (int i = 0; i < n; i++) {
        temp[i] = rand() % 100;
    }
    return temp;
}

int **initMatrix(int n) {
    int **temp = new int *[n];
    for (int i = 0; i < n; i++) {
        temp[i] = initVector(n);
    }
    return temp;
}

int main(int argc, char *argv[]) {
    InitializeCriticalSection(&cs);
    int dims[4] = {100, 1000, 2500, 5000};
    int dims_num = 4;
    int threads = 4;
    fprintf(file, "\\documentclass{article}\n\\usepackage[a4paper, left=0.5cm]{geometry}"
            "\n\\begin{document}\n");

    for (int i = 1; i <= threads; i++) {
        fprintf(file, "\\begin{table}\n");
        print_table_header(i);
        for (int j = 0; j < dims_num; j++) {
            n = dims[j];
            matrix = initMatrix(n);
            vector = initVector(n);
            result = new int[n];
            fprintf(file, "%d\n", n);
            multiply1();
            cout << "multiply2:" << endl;

            threads_num = i;
            current_row = 0;
            multiply2();

            fprintf(file, "\\\\ \\hline\n");
            delete[] result;
        }
        fprintf(file, "\\end{tabular}\n\\end{table}");
    }
    fprintf(file, "\n\\end{document}");

    delete[] vector;
    for (int i = 0; i < n; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    return 0;
}