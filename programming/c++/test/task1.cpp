//
// Created by Drapegnik on 29.10.14.
//
#include <iostream>
#include <string>
#include <climits>
#include <fstream>
#include <cmath>

using namespace std;
ifstream fin("task1in.txt");

struct lifo
{
    long long data;
    lifo *next;
};

bool lifo_empty(lifo*& top)
{
    if (top==NULL)
        return true;
    else
        return false;
}

long long show_top(lifo *&top)
{
    return (top->data);
}

void pop(lifo *&top)
{
    lifo *temp=top;
    top=top->next;
    delete temp;
}

void push(lifo *&top,long long v)
{
    lifo *q=new lifo;
    q->data=v;
    q->next=top;
    top=q;
}

int main()
{
    lifo *q=NULL;
    long long mn=INT_MAX;
    mn+=1;
    long long ml=INT_MAX;
    ml+=2;
    long long abs=INT_MAX;
    abs+=3;

    string s;
    getline(fin,s);
    cout<<s;

    for (int i=0;i<int(s.length());i++)
    {
        if (s[i]=='i')
            push(q,mn);
        if (s[i]=='u')
            push(q,ml);
        if (s[i]=='a')
            push(q,abs);
        if (s[i]>=48 && s[i]<=57)
        {
            bool otr=false;
            if (i!=0)
                if (s[i-1]=='-')
                    otr=true;

            int j=i;
            while (s[i]>=48 && s[i]<=57)
                i++;
            string stemp=s.substr(j,i-j);

            int var=0;
            int osn=1;

            for (int l=int(stemp.length()-1);l>=0;l--)
            {
                var+=int(stemp[l]-'0')*osn;
                osn*=10;
            }
            if (otr==true)
                var=0-var;

            push(q,var);
        }
        if (s[i]==')')
        {
            long long a;
            a=show_top(q);
            pop(q);
            long long b;
            b=show_top(q);
            pop(q);

            if (b==abs)
                push(q,fabs(a));
            else
            {
                long long op;
                op=show_top(q);
                pop(q);
                if (op==mn)
                    push(q,min(a,b));
                else
                    push(q,a*b);
            }
        }
    }
    cout<<"="<<show_top(q);
    return 0;
}
//min(10,min(-10,mul(-1,abs(-100))))=-100
