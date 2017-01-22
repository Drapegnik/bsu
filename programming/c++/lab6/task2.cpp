//
// Created by Drapegnik on 26.10.14.
//
#include <iostream>

using namespace std;

struct node
{
    int newdata,data;
    node *next,*prev;
};

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

int main()
{
    int n,m;
    node *p=NULL,*first,*last;
    cout<<"n,m"<<endl;
    cin>>n>>m;

    for (int i=0;i<n*m;i++)
    {
        int x;
        cin>>x;
        pushback(p,x);
    }
    last=p;

    while (p->prev!=NULL)
        p=p->prev;
    first=p;

    while (p<=last)
    {
        if (p->prev==NULL && p->next==NULL)
        {
            p->newdata=p->data;
            break;
        }

        if (p->prev==NULL)
        {
            p->newdata=max(0,p->next->data);
            p=p->next;
        }

        if (p->next==NULL)
        {
            p->newdata=max(0,p->prev->data);
            break;
        }

        p->newdata=max(p->prev->data,p->next->data);
        p=p->next;

    }

    p=first;

    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            cout<<p->newdata<<" ";
            if (p!=last)
                p=p->next;
        }
        cout<<endl;
    }

    return 0;
}
