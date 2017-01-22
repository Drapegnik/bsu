//
// Created by Drapegnik on 13.10.14.
//
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string s[20];
    int ans[20]={};
    s[0]="==";
    s[1]="++";
    s[2]="--";
    s[3]="<=";
    s[4]=">=";
    s[5]="*=";
    s[6]="+=";
    s[7]="-=";
    s[8]="/=";
    s[9]="||";
    s[10]="&&";
    s[11]="!=";
    s[12]="=";
    s[13]="+";
    s[14]="-";
    s[15]="*";
    s[16]="/";
    s[17]=">";
    s[18]="<";
    int ssize=19;

    string wrong[5];
    wrong[0]="<<";
    wrong[1]=">>";
    int wrongsize=2;

    string cod;

    string filename;
    cout<<"filename?"<<endl;
    cin>>filename;
    ifstream fin(filename);


    while (!fin.eof())
    {
        getline(fin,cod);

        for (int i=0;i<wrongsize;i++)
        {
            int pos=0;
            pos=cod.find(wrong[i],pos);

            while(pos!=-1)
            {
                cod.erase(pos,wrong[i].length());
                pos=cod.find(wrong[i],pos);
            }
        }

        for (int i=0;i<ssize;i++)
        {
            int pos=0;
            pos=cod.find(s[i],pos);

            while(pos!=-1)
            {
                ans[i]++;
                cod.erase(pos,s[i].length());
                pos=cod.find(s[i],pos);
            }
        }
    }

    for (int i=0;i<ssize;i++)
        cout<<s[i]<<" : "<<ans[i]<<endl;
    return 0;
}
