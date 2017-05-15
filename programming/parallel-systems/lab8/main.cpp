#include <iostream>
#include <fstream>
#include "Queue.h"

using namespace std;
using namespace placeholders;

FILE* file = fopen("report.tex", "w");
atomic<int> words_num;
string finish_code = "%%FINISH_CODE%%";
mutex mutex_;
double one_time;

void produce(Queue<string>& q) {
  ifstream fin("input.txt");
  string s;
  while (!fin.eof()) {
    getline(fin, s);
    q.push(s);
  }
  q.push(finish_code);
}

void consume(Queue<string>& q, unsigned int id) {
  string s = q.pop();
  bool is_cur_space;

  while (s != finish_code) {
    unique_lock<mutex> mlock(mutex_);
//    cout << "Consumer#" << id << " popped '" << s << "' " << endl;
    mlock.unlock();

    for (int i = 0; i < s.size(); i++) {
      is_cur_space = (s[i] == ' ');
      if (is_cur_space && i > 0 && s[i - 1] != ' ') {
        words_num++;
      }
    }

    if (s[s.size() - 1] != ' ') {
      words_num++;
    }
    s = q.pop();
  }
  q.push(finish_code);
}

void print_table_header(int consumers) {
  fprintf(file, "\\begin{tabular}{|");
  for (int i = 0; i < consumers * 3 + 1; i++) {
    fprintf(file, "l|");
  }
  fprintf(file, "}\\hline\n");

  for (int i = 0; i < consumers; i++) {
    fprintf(file, "\\multicolumn{3}{|c|}{\\textbf{%d Consumer%s}} & ", i + 1,
            i == 0 ? "" : "s");
  }
  fprintf(file, "\\multicolumn{1}{|c|}{\\textbf{words}} ");
  fprintf(file, "\\\\ \\hline\n");

  for (int i = 0; i < consumers; i++) {
    fprintf(file, "\\textbf{time} & \\textbf{acc} & \\textbf{eff} &");
  }
  fprintf(file, "\\\\ \\hline\n");
  return;
}

void generate_input_file(int words) {
  ofstream fout("input.txt");
  for (int i = 0; i < words; i++) {
    fout << "word" << i + 1;
    for (int j = 1; j <= (rand() % 4 + 1); j++) {
      fout << " ";
    }
    if (rand() % 10 == 4) {
      fout << "\n";
    }
  }
  fout.close();
}

int main() {
  int words[4] = {12345, 123456, 1234567, 12345678};
  int words_size = 4;
  int threads = 4;

  fprintf(file, "\\documentclass{article}\n"
      "\\usepackage[a4paper, left=0.5cm]{geometry}\n"
      "\\begin{document}\n\\begin{table}[]");
  print_table_header(threads);

  for (int k = 0; k < words_size; k++) {
    cout << endl << "START TEST " << words[k] << endl << endl;
    generate_input_file(words[k]);

    for (int i = 0; i < threads; i++) {
      Queue<string> q;
      cout << "with " << i + 1 << " consumers" << endl;
      std::vector<thread> consumers;
      words_num = 0;
      auto start_time = std::chrono::steady_clock::now();

      // producer thread
      thread prod1(bind(produce, ref(q)));

      // consumer threads
      for (int j = 0; j <= i; j++) {
        consumers.push_back(thread(bind(&consume, ref(q), j)));
      }

      prod1.join();
      for (int j = 0; j <= i; j++) {
        consumers[j].join();
      }

      auto end_time = chrono::steady_clock::now();
      auto elapsed = chrono::duration_cast<std::chrono::milliseconds>(
          end_time - start_time).count();
      cout << "words: " << words_num << endl;
      cout << "elapsed: " << elapsed << " ms" << endl;
      cout << "--------------------" << endl;

      if (i == 0) {
        one_time = elapsed;
      }

      double acc = one_time / elapsed;
      fprintf(file, "%lli ms & %.2f & %.2f & ", elapsed, acc, acc / (i + 1));
    }
    fprintf(file, "%d", (int) words_num);
    fprintf(file, "\\\\ \\hline\n");
  }
  fprintf(file, "\\end{tabular}\n\\end{table}\n\\end{document}");
  return 0;
}