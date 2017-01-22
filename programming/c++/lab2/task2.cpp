//
// Created by Drapegnik on 30.09.14.
//
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n,a[100];
    cin>>n;

    for (int i=0;i<n;i++)
        cin>>a[i];

    for (int i=0;i<n-1;i++)
    {
        for (int j=i+1;j<n;j++)
            if (a[i]>a[j])
                swap(a[i],a[j]);
    }

    if (a[n-1]*a[n-2]*a[n-3] > a[n-1]*a[0]*a[1]) {
        for (int i=n-1;i>=n-3;i--)
            cout<<a[i]<<" ";
    } else {
        cout<<a[n-1]<<" "<<a[0]<<" "<<a[1];
    }
    return 0;
}
