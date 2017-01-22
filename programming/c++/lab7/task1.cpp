//
// Created by Drapegnik on 12.11.14.
//
#include <iostream>

using namespace std;

int gcd(int a,int b)
{
    if (a<b)
        swap(a,b);
    if (b==0)
        return a;
    return gcd(b,a%b);
}

class Rational
{
    private:
        int a,b;
        void reduce(Rational &obj)
        {
            int d=gcd(obj.a,obj.b);
            obj.a/=d;
            obj.b/=d;
        }
    public:
        Rational(): a(0), b(1) {}
        Rational(int ch,int zn)
        {
            a=ch;
            if (zn)
                b=zn;
            else
                cout<<"error"<<endl;
            reduce(*this);
        }
        Rational (const Rational &obj)
        {
            a=obj.a;
            b=obj.b;
        }

        void print()
        {
            cout<<a;
            if (b!=1)
                cout<<"/"<<b;
            cout<<endl;
        }
        Rational add(const Rational &obj)
        {
            Rational temp(a*obj.b+b*obj.a,b*obj.b);
            reduce(temp);
            return temp;
        }
        Rational mul(const Rational &obj)
        {
            Rational temp(a*obj.a,b*obj.b);
            reduce(temp);
            return temp;
        }
        Rational div(const Rational &obj)
        {
            Rational temp(a*obj.b,b*obj.a);
            reduce(temp);
            return temp;
        }

        bool Equal(Rational &obj)
        {
            reduce(*this);
            reduce(obj);
            if (a==obj.a && b==obj.b)
                return true;
            else
                return false;
        }

        bool Greater(Rational &obj)
        {
            reduce(*this);
            reduce(obj);
            if ((a*obj.b)>(b*obj.a))
                return true;
            else
                return false;
        }

        bool Less(Rational &obj)
        {
            reduce(*this);
            reduce(obj);
            if ((a*obj.b)<(b*obj.a))
                return true;
            else
                return false;
        }
};

int main()
{
    Rational z1(2,4),z2(1,2);
    z1.print();
    z2.print();
    return 0;
}
