#include <iostream>
#include <fstream>
#include <windows.h>
#include <process.h>

#define CHECK(condition) if (!condition) std::cerr

using namespace std;
FILE *file = fopen("report-part1.tex", "w");
int **matrix;
int *vector, *result;
int n;

int **initMatrix(int n);

unsigned int WINAPI ThreadFunction(void *param) {
    int i = int(param);
    int sum = 0;
    for (int j = 0; j < n; j++)
        sum += matrix[i][j] * vector[j];
    result[i] = sum;
    return 0;
}

void multiply() {
    cout << "n=" << n << " with " << n << " threads: ";
    HANDLE *hThreads = new HANDLE[n];
    LARGE_INTEGER freq, start_time, end_time;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&start_time);

    // create child threads
    for (int i = 0; i < n; i++) {
        hThreads[i] = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction, (void *) i, 0, NULL);
        // error handling
//        CHECK(hThreads[i]) << "Create Thread Error: " << GetLastError() << endl;
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

    delete[] hThreads;
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
    int dims[4] = {100, 1000, 2500, 5000};
    int dims_num = 4;

    fprintf(file, "\\documentclass{article}\n\\usepackage[a4paper, left=0.5cm]{geometry}"
            "\n\\begin{document}\n\\begin{table}\n");
    fprintf(file, "\\begin{tabular}{|c|c|}\\hline\n");
    fprintf(file, "\\textbf{dimensions} & \\textbf{time}\\\\ \\hline\n");

    for (int j = 0; j < dims_num; j++) {
        n = dims[j];
        matrix = initMatrix(n);
        vector = initVector(n);
        result = new int[n];
        fprintf(file, "%d\n", n);
        multiply();
        fprintf(file, "\\\\ \\hline\n");
        delete[] result;
    }
    fprintf(file, "\\end{tabular}\n\\end{table}\n\\end{document}");

    delete[] vector;
    for (int i = 0; i < n; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    return 0;
}