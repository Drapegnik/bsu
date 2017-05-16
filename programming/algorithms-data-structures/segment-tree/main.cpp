//
// Created by Drapegnik on 17.03.14.
//
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

int const INF=-1;
vector <int> a;

int main()
{
    int n;
    fin>>n;
    int sz=n;

    while (sz&(sz-1))
        sz++;

    a=vector <int> (2*sz,INF); // INF - нейтральный
    for (int i=sz;i<sz+n;i++)
        fin>>a[i];

    for (int i=sz-1;i>0;i--)
        a[i]=max(a[i*2],a[i*2+1]);

    int l,r,ans=INF;
    cin>>l>>r;
    l+=sz-1;
    r+=sz-1;
    while (l<=r)
    {
        if (l%2!=0)
        {
            ans=max(ans,a[l]);
            l++;
        }
        if (r%2==0)
        {
            ans=max(ans,a[r]);
            r--;
        }
        r/=2;
        l/=2;
    }
    cout<<ans;
    return 0;
}
