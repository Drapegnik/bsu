//
// Created by Drapegnik on 03.12.14.
//
#include <iostream>

using namespace std;

class Set
{
    public:
        char* p;
        int k;
        Set()
        {
            k=0;
            p=new char;
        }
        Set (int num)
        {
            k=num;
            p=new char [k];
        }
        Set (string a)
        {
            k=a.length();
            p=new char [k];
            for (int i=0;i<k;i++)
                p[i]=a[i];
        }
        Set (const Set &obj)
        {
            k=obj.k;
            p=new char [k];
            p=obj.p;
        }
        ~Set ()
        {
            delete []p;
        }
        Set& operator = (const Set& obj)
        {
            delete []p;
            this->k=obj.k;
            this->p=new char [obj.k];
            for (int i=0;i<k;i++)
                this->p[i]=obj.p[i];
            return *this;
        }
        friend istream& operator >> (istream&, Set&);
        friend ostream& operator << (ostream&, const Set&);
        friend Set operator *(const Set&,const Set&);
        friend Set operator +(const Set&,const Set&);
        friend Set operator -(const Set&,const Set&);
        friend bool operator <(const Set&,const Set&);
        friend bool operator ==(const Set&,const Set&);
};

Set operator *(const Set& a1,const Set& a2)
{
    string s;
    bool *ok=new bool [a2.k];
    for (int i=0;i<a2.k;i++)
        ok[i]=true;
    for (int i=0;i<a1.k;i++)
    {
        for (int j=0;j<a2.k;j++)
            if ((a1.p[i]==a2.p[j]) && (ok[j]))
            {
                s.push_back(a1.p[i]);
                ok[j]=false;
                break;
            }
    }
    delete []ok;
    return Set(s);
}

Set operator +(const Set& a1,const Set& a2)
{
    Set temp(a1.k+a2.k);
    for (int i=0;i<a1.k;i++)
        temp.p[i]=a1.p[i];
    for (int i=a1.k;i<temp.k;i++)
        temp.p[i]=a2.p[i-a1.k];
    return temp;
}

Set operator -(const Set& a1,const Set& a2)
{
    string s;

    bool *us=new bool [a2.k];
    for (int i=0;i<a2.k;i++)
        us[i]=false;

    for (int i=0;i<a1.k;i++)
    {
        bool ok=true;
        for (int j=0;j<a2.k;j++)
            if ((a1.p[i]==a2.p[j]) && (!us[j]))
            {
                ok=false;
                us[j]=true;
                break;
            }
        if (ok)
            s.push_back(a1.p[i]);
    }
    return Set(s);
}

bool operator ==(const Set& a1,const Set& a2) //эквивалентность реализована в понимании равенства двух множеств
{
    if (a1.k!=a2.k)
        return false;
    for (int i=0;i<a1.k;i++)
    {
        bool ok=false;
        for (int j=0;j<a2.k;j++)
            if (a1.p[i]==a2.p[j])
            {
                ok=true;
                break;
            }
        if (!ok)
            return false;
    }
    return true;
}

bool operator <(const Set& a1,const Set& a2)
{
    Set temp=a1*a2;
    if (temp==a1)
        return true;
    else
        return false;
}

istream& operator >> (istream& os, Set& obj)
{
    string s;
    os>>s;
    obj.k=s.length();
    obj.p=new char [obj.k];
    for (int i=0;i<obj.k;i++)
        obj.p[i]=s[i];
    return os;
}

ostream& operator << (ostream& os, const Set& obj)
{
    os<<"{";
    for (int i=0;i<obj.k;i++)
    {
        os<<obj.p[i];
        if (i!=obj.k-1)
            os<<" ";
    }
    os<<"}";
    return os;
}

int main()
{
    Set a,b;

    cout<<"put A and B (like string):"<<endl;
    cin>>a>>b;
    Set c(a);
    c=a*b;
    cout<<"a*b = "<<c<<endl;
    cout<<"a+b = "<<a+b<<endl;
    cout<<"a-b = "<<a-b<<endl;

    cout<<"a=b - ";
    if (a==b)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;

    cout<<"a<b - ";
    if (a<b)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    return 0;
}
