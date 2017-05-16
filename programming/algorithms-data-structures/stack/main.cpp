//
// Created by Drapegnik on 15.10.14.
//
#include <iostream>

using namespace std;

struct lifo
{
    char data;
    lifo *next;
};

bool lifo_empty(lifo*& top)
{
    if (top==NULL)
        return true;
    else
        return false;
}

void show_top(lifo *&top)
{
    cout<<top->data<<endl;
}

void push(lifo *&top,char v)
{
    lifo *q=new lifo;
    q->data=v;
    q->next=top;
    top=q;
}

void pop(lifo *&top)
{
    lifo *temp=top;
    top=top->next;
    delete temp;
}

int main()
{
    lifo *q=NULL;

    return 0;
}
