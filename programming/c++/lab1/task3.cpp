//
// Created by Drapegnik on 17.09.14.
//
#include <iostream>

using namespace std;

int gcd(int a,int b)
{
    if ((b%a)==0)
        return a;
    else
        return gcd(min(a,b%a),max(a,b%a));
}

int main()
{
    int n;
    cin>>n;

    for (int i=1;i<n;i++)
    {
        for (int j=1;j<i;j++)
            if (gcd(j,i)==1)
                cout<<j<<"/"<<i<<endl;
    }
    return 0;
}