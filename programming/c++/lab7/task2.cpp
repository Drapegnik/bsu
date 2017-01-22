//
// Created by Drapegnik on 18.11.14.
//
#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("task2.txt");

class TRAIN
{
    private:
        string dest;
        int num;
        bool exp;
    public:
        TRAIN(): dest("N/A"), num (0), exp (false) {}
        TRAIN(string stacion,int number,bool expres): dest(stacion),num(number), exp(expres) {}
        TRAIN(const TRAIN &obj)
        {
            dest=obj.dest;
            num=obj.num;
            exp=obj.exp;
        }
        void show_train(string stacion)
        {
            if (dest==stacion)
            {
                cout<<"#"<<num<<" "<<dest<<" ";
                if (exp)
                    cout<<"expres"<<endl;
                else
                    cout<<"normal"<<endl;
            }

        }
        void show_epres(string stacion)
        {
            if ((dest==stacion) && (exp))
                cout<<num<<" "<<dest<<" "<<"expres"<<endl;
        }

};

int main()
{
    int n;
    TRAIN p[10];
    fin>>n;
    for (int i=0;i<n;i++)
    {
        string a;
        int b;
        bool c;
        fin>>a>>b>>c;
        TRAIN d(a,b,c);
        p[i]=d;
    }

    string city;
    cout<<"punkt"<<endl;
    cin>>city;
    for (int i=0;i<n;i++)
        p[i].show_train(city);
    cout<<endl;

    cout<<"punkt expres"<<endl;
    cin>>city;
    for (int i=0;i<n;i++)
        p[i].show_epres(city);
    return 0;
}
