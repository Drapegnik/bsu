//
// Created by Drapegnik on 03.03.14.
//
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

vector <bool> us;
vector <vector<int> > g;
vector <int> tin,fup;
int timer=0;

void dfs(int v,int p)
{
    us[v]=true;
    tin[v]=timer;
    fup[v]=timer;
    timer++;
    int child=0;

    for (int i=0;i<g[v].size();i++)
    {
        int to=g[v][i];
        if (to==p)
            continue;
        if (us[to])
            fup[v]=min(fup[v],tin[to]);
        else
        {
            dfs(to,v);
            fup[v]=min(fup[v],fup[to]);
            if (fup[to]>=tin[v] && p!=-1)
                fout<<v+1<<endl;
            child++;
        }
    }
    if (p==-1 && child>1)
        fout<<v+1<<endl;
}

int main()
{
    int n,m;
    fin>>n>>m;
    g=vector <vector<int> > (n);
    us=vector <bool> (n,false);
    tin=vector <int> (n,0);
    fup=vector <int> (n,0);
    for (int j=0;j<m;j++)
    {
        int x,y;
        fin>>x>>y;
        x--; y--;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    dfs(0,-1);
    return 0;
}
