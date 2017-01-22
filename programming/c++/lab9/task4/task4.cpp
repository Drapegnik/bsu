//
// Created by Drapegnik on 08.12.14.
//
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;
ifstream fin("input.txt");

class Array
{
    public:
        int* a;
        int k;
    Array(): k(0)
    {
        a=new int;
    }
    Array(int b,int c=0): k(b)
    {
        delete [] a;
        a=new int [k+1];
        for (int i=0;i<=k;i++)
            a[i]=c;
    }
    /*Array(const Array &obj)
    {
        delete [] a;
        k=obj.k;
        a=new int [k+1];
        for (int i=0;i<=k;i++)
            a[i]=obj.a[i];
    }*/
    /*~Array()
    {
        delete [] a;
    }*/

    virtual void getel()
    {
        delete [] a;
        int n;
        fin>>n;
        k=n;
        a=new int [k+1];
        for (int i=0;i<=k;i++)
            fin>>a[i];
    }

    int& operator[ ](int i)
    {
        if (i<0 || i>k)
        {
            cout<<"error "<<i<<endl;
            exit(1);
        }
        return a[i];
    }
};

class Polinom: public Array
{
    public:
    Polinom(): Array() {}
    Polinom(int b,int c): Array(b,c) {}
    Polinom(const Polinom &obj)
    {
        delete [] a;
        k=obj.k;
        a=new int [k+1];
        for (int i=0;i<=k;i++)
            a[i]=obj.a[i];
    }
    ~Polinom()
    {
      delete [] a;
    }
    void getel()
    {
        Array::getel();
    }
    Polinom& operator = (const Polinom& obj)
    {
        if (&obj==this)
            return *this;

        delete [] a;
        k=obj.k;
        a=new int [k+1];
        for (int i=0;i<=k;i++)
            a[i]=obj.a[i];

        return *this;
    }

    friend Polinom operator + (Polinom&,Polinom&);
    friend Polinom operator - (Polinom&,Polinom&);
    friend Polinom operator * (Polinom&,Polinom&);
    friend bool operator >= (Polinom&,Polinom&);
    friend bool operator <= (Polinom&,Polinom&);
    friend bool operator == (Polinom&,Polinom&);

    int calc(int x)
    {
        int ans=0,deg=1;
        for (int i=0;i<k;i++)
        {
            ans+=a[i]*deg;
            deg*=x;
        }
        return ans;
    }
};

Polinom operator + (Polinom &p1,Polinom &p2)
{
    if (p2.k>p1.k)
    {
        Polinom temp=p2;
        for (int i=0;i<=p1.k;i++)
            temp.a[i]+=p1.a[i];
        return temp;
    }
    else
    {
        Polinom temp=p1;
        for (int i=0;i<=p2.k;i++)
            temp.a[i]+=p2.a[i];
        return temp;
    }
}

Polinom operator - (Polinom &p1,Polinom &p2)
{
    if (p2.k>p1.k)
    {
        Polinom temp=p2;
        for (int i=0;i<=p1.k;i++)
            temp.a[i]=p1.a[i]-temp.a[i];
        for (int i=p1.k+1;i<=p2.k;i++)
            temp.a[i]*=(-1);
        return temp;
    }
    else
    {
        Polinom temp=p1;
        for (int i=0;i<=p2.k;i++)
            temp.a[i]-=p2.a[i];
        return temp;
    }
}

Polinom operator * (Polinom &p1,Polinom &p2)
{
    Polinom temp((p1.k+p2.k),0);
    for (int i=0;i<=p1.k;i++)
        for (int j=0;j<=p2.k;j++)
            temp[i+j]+=p1[i]*p2[j];
    return temp;
}

bool operator >= (Polinom &p1,Polinom &p2)
{
    if (p1.k>p2.k)
        return true;
    else
        if (p1.k<p2.k)
            return false;
        else
        {
            for (int i=p1.k;i>=0;i--)
                if (p1.a[i]<p2.a[i])
                    return false;
            return true;
        }
}

bool operator == (Polinom &p1,Polinom &p2)
{
    if (p1.k!=p2.k)
        return false;
    for (int i=0;i<p1.k;i++)
        if (p1.a[i]!=p2.a[i])
            return false;
    return true;
}

bool operator <= (Polinom &p1,Polinom &p2)
{
    if (p1==p2)
        return true;
    if (p1>=p2)
        return false;
    return true;
}

int main()
{
    Polinom d1,d2;
    d1.getel();
    d2.getel();
    for (int i=0;i<=d1.k;i++)
        cout<<d1[i]<<" ";
    cout<<endl;
    for (int i=0;i<=d2.k;i++)
        cout<<d2[i]<<" ";
    cout<<endl;

    Polinom temp=d1+d2;
    cout<<"d1+d2= ";

    for (int i=0;i<=temp.k;i++)
        cout<<temp.a[i]<<" ";
    cout<<endl;

    temp=d1-d2;
    cout<<"d1-d2= ";

    for (int i=0;i<=temp.k;i++)
        cout<<temp.a[i]<<" ";
    cout<<endl;

    temp=d1*d2;
    cout<<"d1*d2= ";

    for (int i=0;i<=temp.k;i++)
        cout<<temp.a[i]<<" ";
    cout<<endl;

    if (d1==d2)
        cout<<"d1=d2"<<endl;
    if (d1>=d2)
        cout<<"d1>=d2"<<endl;
    if (d1<=d2)
        cout<<"d1<=d2"<<endl;
    return 0;
}
