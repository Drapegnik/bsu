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

char show_top(lifo *&top)
{
    return (top->data);
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
    string s;
    getline(cin,s);
    lifo *q=NULL;

    for (int i=0;i<int(s.length());i++)
    {
        if (s[i]=='x')
            push(q,'x');
        if (s[i]=='n')
            push(q,'n');
        if (s[i]>=48 && s[i]<=57)
            push(q,s[i]);
        if (s[i]==')')
        {
            int a,b;
            char op;
            a=show_top(q)-'0';
            pop(q);
            b=show_top(q)-'0';
            pop(q);
            op=show_top(q);
            pop(q);

            if (op=='x')
                push(q,char(max(a,b)+48));
            else
                push(q,char(min(a,b)+48));
        }
    }
    cout<<show_top(q);
    return 0;
}
