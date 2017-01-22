//
// Created by Drapegnik on 01.12.14.
//
#include <iostream>
#include <fstream>
#include <typeinfo>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

class man
{
    public:
        string name;
        bool pol;
        int vozrst,wes;
    man()
    {
        name="N/A";
        pol=true;
        vozrst=0;
        wes=0;
    }
    man (string a,bool b,int c,int d): name(a), pol(b), vozrst(c), wes(d) {}
    man (const man &obj)
    {
        name=obj.name;
        pol=obj.pol;
        vozrst=obj.vozrst;
        wes=obj.wes;
    }
    void change_name(string a)
    {
        name=a;
    }
    void change_vozrst(int a)
    {
        vozrst=a;
    }
    void change_wes(int a)
    {
        wes=a;
    }
    virtual void get()
    {
        string a;
        bool b;
        int c,d;
        fin>>a>>b>>c>>d;
        name=a;
        pol=b;
        vozrst=c;
        wes=d;
    }
    virtual void show()
    {
        fout<<name<<" "<<pol<<" "<<vozrst<<" "<<wes<<" ";
    }
    virtual bool operator == (man& obj)
    {
        if (vozrst==obj.vozrst)
            return true;
        else
            return false;
    }
};

class student: public man
{
    public:
        int edu;
    student()
    {
        man();
        edu=0;
    }
    student(string a,bool b,int c,int d,int e): man(a,b,c,d),edu(e) {}
    student(const student& obj)
    {
        name=obj.name;
        pol=obj.pol;
        vozrst=obj.vozrst;
        wes=obj.wes;
        edu=obj.edu;
    }
    void change_edu(int a)
    {
        edu=a;
    }
    void plus_edu()
    {
        edu++;
    }
    void get()
    {
        man::get();
        int e;
        fin>>e;
        edu=e;
    }
    void show()
    {
        man::show();
        fout<<edu;
    }
    bool operator == (student& obj)
    {
        if (edu==obj.edu)
            return true;
        else
            return false;
    }
};

int main()
{
    man* ptr[100];
    int na,nb;
    fin>>na;
    man *a=new man [na];
    for (int i=0;i<na;i++)
        a[i].get();

    for (int i=0;i<na;i++)
        ptr[i]=&a[i];

    fin>>nb;
    student *b=new student [nb];
    for (int i=0;i<nb;i++)
        b[i].get();

    for (int i=na;i<na+nb;i++)
        ptr[i]=&b[i-na];

    int n=na+nb;
    for (int i=0;i<n;i++)
    {
        ptr[i]->show();
        fout<<endl;
    }

    int ans1=0,ans2=0;

    bool* us=new bool [n];
    for (int i=0;i<n;i++)
        us[i]=false;

    for (int i=0;i<n;i++)
    {
        for (int j=i+1;j<n;j++)
        {
            student *t1,*t2;
            t1=dynamic_cast <student*> (ptr[i]);
            t2=dynamic_cast <student*> (ptr[j]);

            if (t1)
            {
                if (t2)
                    if (*t1==*t2)
                        {
                            if(!us[i])
                            {
                                ans2++;
                                us[i]=true;
                            }
                            if (!us[j])
                            {
                                ans2++;
                                us[j]=true;
                            }
                        }

            }
            else
                if (!t2)
                    if (*ptr[i]==*ptr[j])
                        {
                            if(!us[i])
                            {
                                ans1++;
                                us[i]=true;
                            }
                            if (!us[j])
                            {
                                ans1++;
                                us[j]=true;
                            }
                        }
        }
    }
    cout<<"kol-vo man odnogo vozrst - "<<ans1<<endl;
    cout<<"kol-vo student odnogo goda - "<<ans2<<endl;
    return 0;
}
