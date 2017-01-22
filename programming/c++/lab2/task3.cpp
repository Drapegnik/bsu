//
// Created by Drapegnik on 24.09.14.
//
#include <iostream>

using namespace std;

int main()
{
    int n,m,a[100]={},b[100]={},sum[100]={},proiz[100]={};
    cin>>n;
    for (int i=0;i<=n;i++)
        cin>>a[i];

    cin>>m;
    for (int i=0;i<=m;i++)
        cin>>b[i];

    for (int i=0;i<=max(m,n);i++)
        sum[i]=a[i]+b[i];

    for (int i=0;i<=n;i++)
        for (int j=0;j<=m;j++)
            proiz[i+j]+=a[i]*b[j];

    cout<<"sum: ";
    for (int i=0;i<=max(m,n);i++)
        cout<<sum[i]<<" ";

    cout<<endl<<"proiz: ";
    for (int i=0;i<=(n+m);i++)
        cout<<proiz[i]<<" ";
    return 0;
}
