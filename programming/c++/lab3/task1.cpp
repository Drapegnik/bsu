//
// Created by Drapegnik on 01.10.14.
//
#include <iostream>

using namespace std;

int n;

int str_sum (int **a, int i)
{
    int ans=0;
    for (int j=0;j<n;j++)
        ans+=a[i][j];

    return ans;
}

int stlb_sum (int **a, int j)
{
    int ans=0;
    for (int i=0;i<n;i++)
        ans+=a[i][j];

    return ans;
}

int main()
{
    cin>>n;
    int **a=new int* [n+1];
    for (int i=0;i<n;i++)
        a[i]=new int [n+1];

    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            cin>>a[i][j];

    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            if (str_sum(a,i)!=stlb_sum(a,j))
            {
                cout<<"no magic"<<endl;
                return 0;
            }

    cout<<"magic"<<endl;

  /*  for (int i=0;i<n;i++)
    {
        for (int j=0;j<n;j++)
            cout<<a[i][j];
        cout<<endl;
    }*/
    delete [] a;
    return 0;
}
