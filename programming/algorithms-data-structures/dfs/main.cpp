//
// Created by Drapegnik on 20.01.14.
//
#include <fstream>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

int n,a[100][100],color[100]={},dfs_timer=0,time_in[100],time_out[100];

void dfs (int num)
{
    fout<<num<<" ";
    time_in[num]=dfs_timer++;
    color[num]=1;
    for (int j=0;j<n;j++)
    {
        if (a[num][j]!=0)
            if (color[j]==0)
                dfs(j);
    }
    color[num]=2;
    time_out[num]=dfs_timer++;
}

int main()
{
    fin>>n;
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            fin>>a[i][j];
    dfs(1);
    return 0;
}
