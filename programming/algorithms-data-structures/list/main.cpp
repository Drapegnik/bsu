//
// Created by Drapegnik on 22.10.14.
//
#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next,*prev;
};

void pushfront (node *&p, int v)
{
    node *q=new node;
    q->prev=NULL;
    q->next=p;
    q->data=v;

    if (p==NULL)
    {return;}


    if (p->prev==NULL)
    {
        p->prev=q;
        p=q;
        return;
    }

    node *temp=new node;
    temp=p->prev;
    p->prev=q;
    q->prev=temp;
    p=q;
}

void pushback (node *&p, int v)
{
    node *q=new node;
    q->prev=p;
    q->next=NULL;
    q->data=v;

    if (p==NULL)
    {
        q->prev=NULL;
        q->next=p;
        p=q;
        return;
    }


    if (p->next==NULL)
    {
        p->next=q;
        p=q;
        return;
    }

    node *temp=new node;
    temp=p->next;
    p->next=q;
    q->next=temp;
    p=q;
}

void pop (node *&p)
{
    if (p==NULL)
    {return;}

    if (p->prev==NULL)
    {
        node *temp=new node;
        temp=p;
        p=p->next;
        p->prev=NULL;
        delete temp;
        return;
    }

    if (p->next==NULL)
    {
        node *temp=new node;
        temp=p;
        p=p->prev;
        p->next=NULL;
        delete temp;
        return;
    }

    node *temp=new node;
    temp=p;
    p=p->prev;
    p->next=p->next->next;
    delete temp;
    return;
}

int main()
{
    node  *p=NULL;
    pushback(p,2);
    pushback(p,3);
    pushback(p,4);
    p=p->prev;
    pop(p);
    cout<<p->data;
    return 0;
}
