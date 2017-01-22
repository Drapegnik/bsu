//
// Created by Drapegnik on 16.01.15.
//
#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("input.txt");

class Human
{
    public:
        char gen;
        Human(): gen('0') {}
        Human(char c): gen(c) {}
        virtual char showgen()=0;
        //friend istream& operator >> (istream& os, Human& obj);
        //friend ostream& operator << (ostream& os, const Human& obj);
};

istream& operator >> (istream& os, Human& obj)
{
    os>>obj.gen;
}

ostream& operator << (ostream& os, Human& obj)
{
    os<<obj.gen;
}

class Boy: public Human
{
    public:
        Boy(): Human() {}
        Boy(char c): Human(c) {}
        char showgen()
        {
            return gen;
        }
};

class Girl: public Human
{
    public:
        Girl(): Human() {}
        Girl(char c): Human(c) {}
        char showgen()
        {
            return gen;
        }
};

int max_gen(Human* arr[],int sz)
{
   /* for (int i=0;i<sz;i++)
    {
        cout<<*(arr[i])<<endl;
    }*/
    int ans=0;
    for (int i=0;i<sz;i++)
    {
        Boy *temp1=dynamic_cast <Boy*> (arr[i]);
        if (temp1)
            for (int j=i+1;j<sz;j++)
            {
                Girl *temp2=dynamic_cast <Girl*> (arr[j]);
                if (temp2)
                    if ((arr[i]->showgen())==(arr[j]->showgen()))
                        ans++;
            }
        else
            for (int j=i+1;j<sz;j++)
            {
                Boy *temp3=dynamic_cast <Boy*> (arr[j]);
                if (temp3)
                    if ((arr[i]->showgen())==(arr[j]->showgen()))
                        ans++;
            }
    }
    return ans;
}

char min_gen (Human* arr[],int sz)
{
    int a=0,b=0,d=0;
    for (int i=0;i<sz;i++)
    {

        switch(arr[i]->showgen())
        {
            case 'A': a++; break;
            case 'B': b++; break;
            case 'D': d++; break;
        }
    }
    int ans=min(a,min(b,d));
    if (ans==a)
        return 'A';
    if (ans==b)
        return 'B';
    if (ans==d)
        return 'D';
}

int main()
{
    Human* ptr[10];
    int n,m;
    char temp;

    fin>>n;
    Boy* a=new Boy [n];
    for (int i=0;i<n;i++)
    {
        fin>>a[i];
        ptr[i]=&a[i];
    }

   // for (int i=0;i<n;i++)
     //   cout<<a[i]<<endl;

    fin>>m;
    Girl* b=new Girl [m];
    for (int i=0;i<m;i++)
    {
        fin>>b[i];
        ptr[i+n]=&b[i];
    }

   // for (int i=0;i<m;i++)
      //  cout<<b[i]<<endl;

    cout<<max_gen(ptr,n+m)<<endl;
    cout<<min_gen(ptr,n+m)<<endl;

   /* for (int i=0;i<n+m;i++)
    {
        cout<<*(ptr[i])<<endl;
    }*/

    return 0;
}
