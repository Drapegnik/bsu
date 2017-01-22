//
// Created by Drapegnik on 24.09.14.
//
#include <iostream>

using namespace std;

int main()
{
    int n,a[2][100]={};
    cin>>n;

    for (int i=0;i<n;i++)
        {
            cin>>a[0][i];
        }

    for (int i=0;i<n;i++)
    {
        if (a[1][i]!=-1)
            {
                a[1][i]=1;
                for (int j=i+1;j<n;j++)
                {
                    if (a[0][i]==a[0][j])
                    {
                        a[1][i]++;
                        a[1][j]=-1;
                    }
                }
            }
    }

    for (int i=0;i<n;i++)
    {
        if (a[1][i]>0 && a[1][i]%2==1)
        {
            cout<<a[0][i];
            return 0;
        }
    }

    return 0;
}
