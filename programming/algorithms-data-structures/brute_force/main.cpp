//
// Created by Drapegnik on 19.03.14.
//
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    int m=1<<n;
    int i=0;
    for (int i=0;i<m;i++)
    {
        for (int j=0;j<n;j++)
        {
            int x=(i>>j)&1;
            cout<<x;
        }
        cout<<endl;
    }
    return 0;
}
