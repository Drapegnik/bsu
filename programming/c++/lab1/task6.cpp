//
// Created by Drapegnik on 22.09.14.
//
#include <iostream>

using namespace std;

int gener (int kolvo,int numb)
{
    int a=numb;
    kolvo--;
    while (kolvo>0)
    {
        a*=10;
        a+=numb;
        kolvo--;
    }
    return a;
}

int main()
{
    int k,osn=10,kolvo=1;
    cin>>k;

    if (k==1)
    {
        cout<<1;
        return 0;

    }
    while ((k/osn)!=0)
        {
            osn*=10;
            kolvo++;
        }

    osn/=10;

    int numb=k/osn;

    int ans=k+1;

    while (ans%k!=0)
    {
        if (numb==9)
        {
            numb=1;
            kolvo++;
        }

        ans=gener(kolvo,numb);

        numb++;

        if (ans<0)
        {
            cout<<"no solution"<<endl;
            return 0;
        }
    }

    cout<<ans<<"="<<k<<"*"<<ans/k;
    return 0;
}