//
// Created by Drapegnik on 23.03.14.
//
#include <fstream>
#include <vector>
#include <climits>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

struct edge
{
    int a,b,cost;
};

int main()
{
    edge rebr;
    int n,m=0,s;
    int const INF=INT_MAX;
    fin>>n>>s;
    s--;
    vector <edge> e;
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
        {
            int x;
            fin>>x;
            if (x!=0)
            {
                rebr.a=i;
                rebr.b=j;
                rebr.cost=x;
                e.push_back(rebr);
                m++;
            }
        }
    vector <int> d(n+1,INF);

    d[s]=0;

    for (;;)
    {
        bool any=false;
        for (int i=0;i<m;i++)
            if (d[e[i].a]<INF)
                if (d[e[i].b]>d[e[i].a]+e[i].cost)
                {
                    d[e[i].b]=d[e[i].a]+e[i].cost;
                    any=true;
                }
        if (!any)
            break;
    }

    for (int i=0;i<n;i++)
        fout<<d[i]<<" ";
    return 0;
}
