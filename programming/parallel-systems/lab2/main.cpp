#include <iostream>
#include <fstream>
#include <windows.h>
#include <process.h>
#include <cmath>
#include <cstdlib>
#include <chrono>

#define CHECK(condition) if (!condition) std::cerr

using namespace std;
FILE *file = fopen("report.tex", "w");
double one_time, *pi;
int n, threads_num;

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

    if (threads_num == 1) {
        one_time = hq_elapsed;
    }

    cout << "pi=" << sum << endl;
    cout << "GetTickCount time=" << win_elapsed << " ms" << endl;
    cout << "cpp1 time=" << cpp11_elapsed << " ms" << endl;
    cout << "QueryPerformance time=" << hq_elapsed << " ms" << endl;

    fprintf(file, " & %.3f & %.3f & %.3f", hq_elapsed, one_time / hq_elapsed, hq_elapsed / threads_num);
    return sum;
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

int main(int argc, char *argv[]) {
    int dims[4] = {100000, 1000000, 10000000, 100000000};
    int dims_num = 4;
    int threads = 4;

    fprintf(file, "\\documentclass{article}\n\\usepackage[a4paper, left=0.5cm]{geometry}\n\\begin{document}\n\\begin{table}[]");
    print_table_header(threads);
    for (int i = 0; i < dims_num; i++) {
        n = dims[i];
        fprintf(file, "%d\n", n);
        for (int j = 0; j < threads; j++) {
            threads_num = j + 1;
            count_pi();
        }
        fprintf(file, "\\\\ \\hline\n");
    }
    fprintf(file, "\\end{tabular}\n\\end{table}\n\\end{document}");
    return 0;
}