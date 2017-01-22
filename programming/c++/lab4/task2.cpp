//
// Created by Drapegnik on 08.10.14.
//
#include <iostream>
#include <string>

using namespace std;

int main()
{
    while (!cin.eof())
    {
        string s;
        cin>>s;
        for (int i=0;i<int(s.length()/2);i++)
            swap(s[i],s[s.length()-1-i]);

        cout<<s<<" ";
    }
    return 0;
}
