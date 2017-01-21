//
// Created by Drapegnik on 17.09.14.
//
#include <iostream>

using namespace std;

int main()
{
    long long n,osn=10,ans=0;
    cin>>n;

    for (long long i=1;i<n;i++)
    {
        if ((i/osn)!=0)
            osn*=10;

        long long a=(i*i)%osn;
        if (a==i)
        {
            cout<<i<<" "<<i*i<<endl;
            ans++;
        }
    }
    cout<<ans;
    return 0;
}