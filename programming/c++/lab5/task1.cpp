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
    cin>>s;
    lifo *q=NULL;
    for (int i=0;i<int(s.length());i++)
    {
        if ((s[i]=='(') || (s[i]=='[') || (s[i]=='{'))
            push(q,s[i]);
        if ((s[i]==')') || (s[i]==']') || (s[i]=='}'))
            if (lifo_empty(q)==true)
            {
                cout<<"wrong"<<endl;
                return 0;
            }
            else
            {
                if (s[i]==')')
                    if (show_top(q)=='(')
                        pop(q);
                    else
                    {
                        cout<<"wrong"<<endl;
                        return 0;
                    }

                if (s[i]==']')
                    if (show_top(q)=='[')
                        pop(q);
                    else
                    {
                        cout<<"wrong"<<endl;
                        return 0;
                    }

                if (s[i]=='}')
                    if (show_top(q)=='{')
                        pop(q);
                    else
                    {
                        cout<<"wrong"<<endl;
                        return 0;
                    }
            }
    }
    if (lifo_empty(q)==true)
        cout<<"correct"<<endl;
    else
        cout<<"wrong"<<endl;
    return 0;
}
