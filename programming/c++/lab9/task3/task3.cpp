//
// Created by Drapegnik on 08.12.14.
//
#include <iostream>

using namespace std;

class series
{
    public:
        int first,step;

        series(): first(0),step(0) {}
        series(int a,int b): first(a), step(b) {}

        virtual int element(int)=0;
        virtual int sum(int)=0;
};

class liner: public series
{
    public:
        liner(): series() {}
        liner(int a,int b): series(a,b) {}
        int element(int n)
        {
            return (first+step*(n-1));
        }
        int sum (int n)
        {
            return ((first+element(n))*n/2);
        }
};

class exp: public series
{
    public:
        exp(): series() {}
        exp(int a,int b): series(a,b) {}
        int element(int n)
        {
            int temp=1;
            for (int i=0;i<n-1;i++)
                temp*=step;
            return (first*temp);
        }
        int sum (int n)
        {
            if (step!=1)
                return ((element(n)*step-first)/(step-1));
            else
                return(n*first);
        }

};


int main()
{
    int t1,t2,n;
    cout<<"vvedi a i d dlya arifmet"<<endl;
    cin>>t1>>t2;
    liner a(t1,t2);
    cout<<"vvedi b i q dlya geometr"<<endl;
    cin>>t1>>t2;
    exp b(t1,t2);

    cout<<"vvedi kol-vo chlenov"<<endl;
    cin>>n;

    series* ptr[2];

    ptr[0]=&a;
    ptr[1]=&b;

    cout<<"liner:   exp:"<<endl;
    for (int i=1;i<=n;i++)
        cout<<ptr[0]->element(i)<<"    "<<ptr[1]->element(i)<<endl;

    cout<<"summa:"<<endl;
    cout<<ptr[0]->sum(n)<<" "<<ptr[1]->sum(n)<<endl;
    return 0;
}
