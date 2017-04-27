#include <iostream>
#include <fstream>
#include <windows.h>
#include <process.h>
#include <cmath>

#define CHECK(condition) if (!condition) std::cerr

struct ThreadParams {
    int start, end;
};

using namespace std;
FILE *file = fopen("report.tex", "w");
int **matrix;
int *vector, *result;
int n, threads_num;
double one_time;

int **initMatrix(int n);

unsigned int WINAPI ThreadFunction(void *params) {
    ThreadParams *p = (ThreadParams *) params;
    for (int i = p->start; i < p->end; i++) {
        int sum = 0;
        for (int j = 0; j < n; j++)
            sum += matrix[i][j] * vector[j];
        result[i] = sum;
    }
    return 0;
}

int *multiply() {
    cout << "n=" << n << " with " << threads_num << " threads: ";
    HANDLE *hThreads = new HANDLE[threads_num];
    ThreadParams *params = new ThreadParams();
    int q = n / threads_num;
    int r = n % threads_num;
    int i = 0;
    int j = 0;
    LARGE_INTEGER freq, start_time, end_time;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&start_time);

    // create child threads
    while (i < n) {
        int num = (r == 0) ? q : q + 1;
        params->start = i;
        i += num;
        params->end = i;
        if (r > 0) { r--; }
        hThreads[j++] = (HANDLE) _beginthreadex(NULL, 0, ThreadFunction, (void *) params, 0, NULL);
        // error handling
        CHECK(hThreads[j - 1]) << "Create Thread Error: " << GetLastError() << endl;
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
    fprintf(file, " & %.3f & %.3f & %.3f", elapsed, one_time / elapsed, elapsed / threads_num);
    return result;
}

void print_table_header(int threads) {
    fprintf(file, "\\begin{tabular}{|");
    for (int i = 0; i < threads * 3 + 1; i++) {
        fprintf(file, "l|");
    }
    fprintf(file, "}\\hline\n");
    fprintf(file, "\\multicolumn{1}{|c|}{\\textbf{dimensions}} ");

    for (int i = 0; i < threads; i++) {
        fprintf(file, "& \\multicolumn{3}{c|}{\\textbf{%d Thread%s}} ", i + 1, i == 0 ? "" : "s");
    }
    fprintf(file, "\\\\ \\hline\n");

    for (int i = 0; i < threads; i++) {
        fprintf(file, " & \\textbf{time} & \\textbf{acc} & \\textbf{eff}");
    }
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
    int dims[4] = {2500, 5000, 7500, 10000};
    int dims_num = 4;
    int threads = 4;

    fprintf(file, "\\documentclass{article}\n\\usepackage[a4paper, left=0.5cm]{geometry}"
            "\n\\begin{document}\n\\begin{table}[]");
    print_table_header(threads);
    for (int i = 0; i < dims_num; i++) {
        n = dims[i];
        matrix = initMatrix(n);
        vector = initVector(n);
        result = new int[n];

        fprintf(file, "%d\n", n);
        for (int j = 1; j <= threads; j++) {
            threads_num = j;
            multiply();
        }
        fprintf(file, "\\\\ \\hline\n");
    }
    fprintf(file, "\\end{tabular}\n\\end{table}\n\\end{document}");
    return 0;
}