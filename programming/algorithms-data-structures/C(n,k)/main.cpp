//
// Created by Drapegnik on 18.03.14.
//
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n,k;
    cin>>n>>k;
    vector <int> a(n+1,1);
    for (int i=1;i<n;i++)
        for (int j=i;j>=1;j--)
            a[j]+=a[j-1];

    cout<<a[k];
    return 0;
}
