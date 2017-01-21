//
// Created by Drapegnik on 17.09.14.
//
#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int ans=0,n;
    cin>>n;

    for (int i=1;i<n;i++)
    {
        int sum=0,k=0;
        for (int j=1;j<=(i/2);j++)
        {
            if ((i%j)==0)
            {
                k++;
                sum+=j;
            }
            if (sum>i)
                break;
        }
        if (sum==i && k!=1)
        {
            cout<<i<<endl;
            ans++;
        }
        sum=0;
        k=0;

    }
    cout<<ans;
    return 0;
}