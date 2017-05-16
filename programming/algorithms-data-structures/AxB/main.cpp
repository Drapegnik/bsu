//
// Created by Drapegnik on 22.02.14.
//
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
   string s;

   fin>>s;
   int k1=s.length();
   vector <int> a(k1);
   for (int i=0;i<k1;i++)
        a[i]=s[k1-1-i]-'0';

   fin>>s;
   int k2=s.length();
   vector <int> b(k2);
   for (int i=0;i<k2;i++)
        b[i]=s[k2-1-i]-'0';

   int k=k1+k2+1;
   vector <int> c(k+1,0);

   for (int i=0;i<k1;i++)
    for (int j=0;j<k2;j++)
        c[i+j]+=a[i]*b[j];

   for (int i=0;i<k;i++)
   {
       c[i+1]+=c[i]/10;
       c[i]%=10;
   }
   while (c[k]==0)
    k--;

   for (int i=k;i>=0;i--)
    fout<<c[i];
   return 0;
}
