//
// Created by Drapegnik on 26.10.14.
//
#include <iostream>
#include <climits>

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
    if (p->prev==NULL && p->next==NULL)
    {
        p=NULL;
        return;
    }

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
    int n;
    node *p=NULL,*ans=NULL;
    cin>>n;
    for (int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        pushback(p,x);
    }

    while (p!=NULL)
    {
        node *mn=new node;
        mn->data=INT_MAX;

        while (p->prev!=NULL)
            p=p->prev;

        while (p->next!=NULL)
        {
            if (p->data<mn->data)
                mn=p;
            p=p->next;
        }
        if (p->data<mn->data)
                mn=p;

        pushback(ans,mn->data);
        p=mn;
        pop(p);
        n--;
    }
    while (ans->prev!=NULL)
        ans=ans->prev;

    while (ans->next!=NULL)
    {
        cout<<ans->data<<" ";
        ans=ans->next;
    }
    cout<<ans->data;
    return 0;
}
