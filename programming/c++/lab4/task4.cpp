//
// Created by Drapegnik on 13.10.14.
//
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s,s1,s2;
    cin>>s>>s1>>s2;

    int k1=s1.length(),k2=s2.length();

    while (s.find(s1,0)<=s.length())
    {
        int pos=s.find(s1,0);
        s.replace(pos,k1,s2,0,k2);
    }
    cout<<s;
    return 0;
}
