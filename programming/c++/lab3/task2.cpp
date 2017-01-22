//
// Created by Drapegnik on 01.10.14.
//
#include <iostream>
#include <climits>

using namespace std;

int n;
const int MX=INT_MAX;

int* minel (int *a)
{
    int mn=0;
    for (int i=0;i<n;i++)
        if (a[i]<a[mn])
           mn=i;
    return &a[mn];
}

int main()
{
    cin>>n;
    int *a=new int [n];
    int *b=new int [n];
    for (int i=0;i<n;i++)
        cin>>a[i];

    for (int i=0;i<n;i++)
    {
        b[i]=(*minel(a));
        *minel(a)=INT_MAX;
    }

    for (int i=0;i<n;i++)
        cout<<b[i]<<" ";

    delete [] a;
    delete [] b;
    return 0;
}
