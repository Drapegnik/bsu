//
// Created by Drapegnik on 17.09.14.
//
#include <iostream>
#include <fstream>
#include <typeinfo>

using namespace std;
ifstream fin("task2in.txt");
ofstream fout("task2out.txt");

int const base=660;

class man
{
    public:
        string name;
        bool pol;
        int vozrst;
    man()
    {
        name="N/A";
        pol=true;
        vozrst=0;
    }
    man (string a,bool b,int c): name(a), pol(b), vozrst(c) {}

    void change_name(string a)
    {
        name=a;
    }
    void change_vozrst(int a)
    {
        vozrst=a;
    }
    virtual void get()=0;
    virtual void show()=0;
    virtual void change_step()=0;
};

class student: public man
{
    public:
        double avg;
        int cource,step;
        string spec;
    student(): man(), avg(0),cource(0),step(0),spec("N/A") {}
    student(string a,bool b,int c,int d,int e,string h,int f): man(a,b,c), avg(d), cource(e),spec(h),step(f) {}
    student(const student &obj) //конструктор копирования
    {
        name=obj.name;
        pol=obj.pol;
        vozrst=obj.vozrst;
        avg=obj.avg;
        cource=obj.cource;
        step=obj.step;
        spec=obj.spec;
    }

    void get()
    {
        string a,h;
        bool b;
        int c,e,f;
        double d;
        fin>>a>>b>>c>>d>>e>>h>>f;
        name=a;
        pol=b;
        vozrst=c;
        avg=d;
        cource=e;
        spec=h;
        step=f;
    }

    void show()
    {
        fout<<name<<"\t"<<pol<<"\t"<<vozrst<<"\t"<<avg<<"\t"<<cource<<"\t"<<spec<<"\t"<<step<<endl;
    }

    void change_step()
    {
        double koef=1;
        if (avg>=5)
            koef=2;
        else
            koef=0.5;
        step=base*koef;
    }

    student& operator = (const student& obj)
    {
        if (&obj==this)
            return *this;

        name=obj.name;
        pol=obj.pol;
        vozrst=obj.vozrst;
        avg=obj.avg;
        cource=obj.cource;
        step=obj.step;
        spec=obj.spec;

        return *this;
    }

};

class aspirant: public man
{
    public:
        double avg;
        int year,step;
        string spec;
    aspirant(): man(), avg(0),year(0),step(0),spec("N/A") {}
    aspirant(string a,bool b,int c,int d,int e,string h,int f): man(a,b,c), avg(d), year(e),spec(h),step(f) {}
    aspirant(const aspirant &obj) //конструктор копирования
    {
        name=obj.name;
        pol=obj.pol;
        vozrst=obj.vozrst;
        avg=obj.avg;
        year=obj.year;
        step=obj.step;
        spec=obj.spec;
    }
    void get()
    {
        string a,h;
        bool b;
        int c,e,f;
        double d;
        fin>>a>>b>>c>>d>>e>>h>>f;
        name=a;
        pol=b;
        vozrst=c;
        avg=d;
        year=e;
        spec=h;
        step=f;
    }
    void show()
    {
        fout<<name<<"\t"<<pol<<"\t"<<vozrst<<"\t"<<avg<<"\t"<<year<<"\t"<<spec<<"\t"<<step<<endl;
    }

    void change_step()
    {
        step=base*3;
    }
    aspirant& operator = (const aspirant& obj)
    {
        if (&obj==this)
            return *this;

        name=obj.name;
        pol=obj.pol;
        vozrst=obj.vozrst;
        avg=obj.avg;
        year=obj.year;
        step=obj.step;
        spec=obj.spec;

        return *this;
    }
};

int main()
{
    student* a;
    int n;
    fin>>n;

    a=new student [n];
    for (int i=0;i<n;i++)
        a[i].get();

    aspirant* b;
    int k;
    fin>>k;

    b=new aspirant [k];
    for (int i=0;i<k;i++)
        b[i].get();

    man* ptr[100];

    for(int i=0;i<n;i++)
        ptr[i]=&a[i];

    for(int i=n;i<n+k;i++)
        ptr[i]=&b[i-n];

    int sz=n+k;

    for (int i=0;i<sz;i++)
        ptr[i]->show();

    for (int i=0;i<sz;i++)
    {
        student* t;
        t=dynamic_cast <student*> (ptr[i]);
        if (t)
            ptr[i]->change_step();
    }

    fout<<endl<<endl;

    for (int i=0;i<sz;i++)
        ptr[i]->show();

    fout<<endl<<endl;

    string ans;

    cin>>ans;

    for (int i=0;i<sz;i++)
    {
        student* t1;
        t1=dynamic_cast <student*> (ptr[i]);
        if (t1)
        {
            if (t1->spec==ans)
                t1->show();
        }
        else
        {
            aspirant* t2;
            t2=dynamic_cast <aspirant*> (ptr[i]);
            if (t2->spec==ans)
                t2->show();
        }
    }
    return 0;
}
