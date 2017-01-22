//
// Created by Drapegnik on 07.10.14.
//
#include <iostream>

using namespace std;

int* binsearch (int* a,int x,int l,int r)
{
    int n=r+1;

    if (n==0)
        return &a[0];

    int p=(l+r)/2;
    if (a[p]==x)
    {
        while (a[p]==x)
            p++;
        return &a[p];
    }

    if (r==l)
        if (a[r]>x)
            return &a[r];
        else
            return &a[r+1];

    if (r<0 || l<0)
        return &a[0];

    if (r>n-1 || l>n-1)
        return &a[n];

    if (a[p]>x)
        return binsearch(a,x,l,p-1);
    if (a[p]<x)
        return binsearch(a,x,p+1,r);
}

int main()
{
    int n;
    cin>>n;
    int *a=new int [n+1];
    int *b=new int [2*(n+1)];

    for (int i=0;i<n;i++)
        cin>>a[i];

    int bsize=0;

    for (int i=0;i<n;i++)
    {
        int *q=binsearch(b,a[i],0,bsize-1);
        bsize++;

        for (int* j=&b[bsize];j>q;j--)
            *j=*(j-1);
        *q=a[i];


    }
    for (int i=0;i<bsize;i++)
            cout<<b[i]<<" ";

    delete [] a;
    delete [] b;
    return 0;
}
