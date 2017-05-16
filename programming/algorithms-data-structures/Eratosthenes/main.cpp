//
// Created by Drapegnik on 03.01.14.
//
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
ofstream fout("out.txt");
int main()
{
    int n;
    cin>>n;
    vector <int> v(n,1);

    for (int i=2;i*i<=n;i++)
    {
        if (v[i]==1)
            for (int j=i*i;j<=n;j+=i)
                v[j]=0;
    }

    for (int i=2;i<=n;i++)
        if (v[i]==1)
            fout<<i<<",";
    return 0;
}
