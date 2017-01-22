//
// Created by Drapegnik on 17.09.14.
//
#include <iostream>

using namespace std;

int main()
{
    int a[10]={},n,ans=0;
    cin>>n;

    while (n) // привет
    {
        int x=n%10;
        n/=10;

        if (a[x]!=1)
        {
            ans++;
            a[x]=1;
        }
    }

    cout<<ans<<endl;
    return 0;
}