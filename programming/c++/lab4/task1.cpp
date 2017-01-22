//
// Created by Drapegnik on 12.10.14.
//
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
ifstream fin("task1.txt");

int main()
{
    string s;
    string ans[100];
    int asize=0;

    while (!fin.eof())
    {
        fin>>s;
        for (int i=0;i<int(s.length());i++)
        {
            if ((int(s[i])<65) || (int(s[i])>90 && int(s[i])<97) || (int(s[i])>122))
            {
                s.erase(i,1);
                i--;
            }

        }
        if (s.length()==2)
        {
            ans[asize]=s;
            asize++;
        }

    }
    for (int i=0;i<=asize;i++)
        for (int j=i+1;j<asize;j++)
            if (ans[i]>ans[j])
                swap(ans[i],ans[j]);

   // for (int i=0;i<=asize;i++)
     //   cout<<ans[i]<<" ";

    //cout<<endl;

    for (int i=0;i<asize;i++)
    {
        int k=1;
        cout<<ans[i]<<" ";
        int j=i+1;
        while (ans[j]==ans[i])
            {
                k++;
                j++;
            }
        cout<<k<<endl;
        i=j-1;
    }
    return 0;
}
