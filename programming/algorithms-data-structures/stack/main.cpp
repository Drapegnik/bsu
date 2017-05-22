//
// Created by Drapegnik on 15.10.14.
//
#include <iostream>

using namespace std;

struct lifo {
  char data;
  lifo* next;
};

bool is_lifo_empty(lifo*& top) {
  return (top == NULL);
}

void show_top(lifo*& top) {
  if (!is_lifo_empty(top)) {
    cout << top->data << endl;
  }
}

void push(lifo*& top, char v) {
  lifo* q = new lifo;
  q->data = v;
  q->next = top;
  top = q;
}

void pop(lifo*& top) {
  lifo* temp = top;
  top = top->next;
  delete temp;
}

int main() {
  lifo* q = NULL;
  push(q, '2');
  show_top(q);
  push(q, '3');
  push(q, '4');
  pop(q);
  show_top(q);
  pop(q);
  pop(q);
  cout << (is_lifo_empty(q) ? "empty" : "not empty");
  return 0;
}
