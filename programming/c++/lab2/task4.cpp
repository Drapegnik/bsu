//
// Created by Drapegnik on 30.09.14.
//
#include <iostream>
#include <string>

using namespace std;

int value (char a)
{
    if (a=='I')
        return 1;
    if (a=='V')
        return 5;
    if (a=='X')
        return 10;
    if (a=='L')
        return 50;
    if (a=='C')
        return 100;
    if (a=='D')
        return 500;
    if (a=='M')
        return 1000;

}

int main()
{
    int ans=0;
    string s;
    cin>>s;
    int n=s.length();

    if (n==1)
    {
        cout<<value(s[0]);
        return 0;
    }

    for (int i=0;i<n;i++)
    {
        if (value(s[i])>=value(s[i+1]))
            ans+=value(s[i]);
        else
            ans-=value(s[i]);
    }

    cout<<ans;

    return 0;
}
