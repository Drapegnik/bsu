//
// Created by Drapegnik on 02.12.14.
//
#include <iostream>
#include <fstream>
#include <math.h>
#include <typeinfo>
#include <iomanip>

using namespace std;
ifstream fin("input.txt");

int gcd(int a,int b) //для сокращения обычных дробей
{
    if (a<b)
        swap(a,b);
    if (b==0)
        return a;
    return gcd(b,a%b);
}

int comon(int &a,int &b,bool change) //функция для получения у двух чисел одинакового кол-ва знаков после запяттой
{
    int temp,numa=0,numb=0;
    temp=fabs(a);
    while (temp>0)
    {
        temp/=10;
        numa++;
    }
    temp=fabs(b);
    while (temp>0)
    {
        temp/=10;
        numb++;
    }
    if (change==true)
    {
        if (numa>numb)
            for (int i=0;i<(numa-numb);i++)
                b*=10;
        else
            for (int i=0;i<(numb-numa);i++)
                a*=10;
    }

     temp=1;
     for (int i=0;i<(max(numa,numb));i++)
        temp*=10;
    return temp;
}

class Fraction
{
    public:

        int intp, fract;
        Fraction(): intp(0),fract(0) {} //конструктор без параметров
        Fraction(double a)   //конструктор переводит double к нашему типу
        {
            intp=int(a);  //получение целой части
            double b;
            double* c=&b;
            fract=modf(a,c)*1000000000;   //получение дробной части (с этим есть некоторые проблемы из-за округления doubla
            if (fract!=0)                 //как я не пытался их решить, я не смог. расммотрел много способов...
                while (fmod(fract,10)==0)
                    fract/=10;
            fract=fabs(fract);
        }
        Fraction(int a): intp(a),fract(0) {} //конструктор с одним параметром для перевода int в Fractional
        Fraction(int a,int b): intp(a),fract(b) {} //конструктор с двумя параметрами
        Fraction(const Fraction &obj) //конструктор копирования
        {
            intp=obj.intp;
            fract=obj.fract;
        }

        friend bool operator <= (Fraction, Fraction); //операторы перегрузки дружественные для того,
        friend bool operator >= (Fraction, Fraction); //чтобы работала запись 10+a, где a-Fractional
        friend Fraction operator + (Fraction, Fraction);
        friend Fraction operator - (Fraction, Fraction);
        friend istream& operator >> (istream& os, Fraction& obj);
        friend ostream& operator << (ostream& os, const Fraction& obj);

        Fraction operator = (Fraction const &obj)
        {
            intp=obj.intp;
            fract=obj.fract;
            return *this;
        }
        virtual void func() //функция для того, чтобы сделать классы полиморфными
        {

        };
};

istream& operator >> (istream& os, Fraction& obj)
{
    double a;  //чтение как double
    os>>a;
    obj=a;
    //os>>obj.intp>>obj.fract;  // - вот так через int'ы
    return os;
}
ostream& operator << (ostream& os, const Fraction& obj)
{
    if (obj.fract<0)
        os<<"-";

    os<<obj.intp;

    if (obj.fract!=0)
        os<<"."<<fabs(obj.fract);
    return os;
}

bool operator <= (Fraction f1, Fraction f2)
{
    comon(f1.fract,f2.fract,true);
    if (f1.intp<f2.intp)
        return true;
    if (f1.intp==f2.intp)
        if (f1.fract<=f2.fract)
            return ((f1.intp>=0) ? true : false);     //если числа отрицательные всё наоборот
        else
            return ((f1.intp>=0) ? false : true);
    return false;
}

bool operator >= (Fraction f1, Fraction f2)
{
    comon(f1.fract,f2.fract,true);
    if (f1.intp>f2.intp)
        return true;
    if (f1.intp==f2.intp)
        if (f1.fract>=f2.fract)
            return ((f1.intp>0) ? true : false); //если числа отрицательные всё наоборот
        else
            return ((f1.intp>0) ? false : true);
    return false;

}

Fraction operator + (Fraction f1, Fraction f2)
{
    if (f1<=0) //для отрицательных
        return (f2-Fraction(fabs(f1.intp),fabs(f1.fract)));
    if (f2<=0) //для отрицательных
        return (f1-Fraction(fabs(f2.intp),fabs(f2.fract)));

    int n=comon(f1.fract,f2.fract,true);
    Fraction temp(f1.intp+f2.intp+(f1.fract+f2.fract)/n,(f1.fract+f2.fract)%n);

    if (temp.fract<0) //случай из-за хранения знака в дробной части
    {
        temp.intp--;
        int tmp=1;
        temp.fract+=tmp*comon(temp.fract,tmp,false);
    }
    return temp;
}

Fraction operator - (Fraction f1, Fraction f2)
{
    int sign=1;
    if (f1<=f2)
    {
        swap(f1,f2);
        sign=-1;
    }
    comon(f1.fract,f2.fract,true);
    Fraction temp(f1.intp-f2.intp,f1.fract-f2.fract);
    if (temp.fract<0)
    {
        temp.intp--;
        int tmp=1;
        temp.fract+=tmp*comon(temp.fract,tmp,false);
    }
    if (temp.intp!=0)
        temp.intp*=sign; //знак
    else
        temp.fract*=sign; //если целая часть 0, то знак храниться в дробной
    return temp;
}

class comfract: public Fraction //производный класс
{
    public:
        int osn;

        friend void reduce(comfract&); //собс-но функция сокращения обычных дробей
        comfract()      //конструктор без параметров
        {
            Fraction();
            osn=1;
        }
        comfract(int a,int b,int c)         //конструктор с трюмя параметрами
        {
            intp=a;
            fract=b;
            osn=c;
        }
        comfract(Fraction obj)              //конструктор приведения
        {
            int temp=1;
            intp=obj.intp;
            fract=obj.fract;
            osn=comon(temp,fract,false);
            reduce(*this);
        }
        comfract(comfract const &obj)        //конструктор копированя
        {
            intp=obj.intp;
            fract=obj.fract;
            osn=obj.osn;
        }
        comfract(int a)                     // перевод из int'a
        {
            intp=a;
            fract=0;
            osn=1;
        }
        comfract (double a)
        {
            Fraction temp=a;
            intp=temp.intp;
            fract=temp.fract;
            int e=1;
            osn=comon(e,fract,false);
            reduce(*this);
        }
        friend comfract operator + (comfract, comfract);
        friend void operator += (comfract&, comfract);

        comfract operator = (comfract const &obj)
        {
            intp=obj.intp;
            fract=obj.fract;
            osn=obj.osn;
            return *this;
        }

        friend istream& operator >> (istream& os, comfract& obj);
        friend ostream& operator << (ostream& os, const comfract& obj);
        void func() //функция для того, чтобы сделать классы полиморфными
        {

        };

};

istream& operator >> (istream& os, comfract& obj)
{
    os>>obj.intp>>obj.fract>>obj.osn;
}
ostream& operator << (ostream& os, const comfract& obj)
{
    if (obj.fract<0)
        os<<"-";

    os<<obj.intp;

    if (obj.fract!=0)
    {
        os<<" "<<fabs(obj.fract);
        if (obj.osn!=1)
            os<<"/"<<obj.osn;
    }

    return os;
}


void reduce(comfract& obj)
{
    int d=gcd(obj.fract,obj.osn);
    obj.fract/=d;
    obj.osn/=d;
}

comfract operator + (comfract c1, comfract c2)
{
    comfract temp;
    temp.intp=c1.intp+c2.intp;
    temp.osn=c1.osn*c2.osn;
    temp.fract=c1.fract*c2.osn+c2.fract*c1.osn;
    reduce(temp);
    temp.intp+=temp.fract/temp.osn;
    temp.fract%=temp.osn;
    return temp;
}

void operator += (comfract& c1, comfract c2)
{
    c1=c1+c2;
}

int main()
{
    Fraction* ptr[100];
    int na,nb;
    fin>>na;
    Fraction *a=new Fraction [na];
    for (int i=0;i<na;i++)
        fin>>a[i];

    for (int i=0;i<na;i++)
        ptr[i]=&a[i];

    fin>>nb;
    comfract *b=new comfract [nb];
    for (int i=0;i<nb;i++)
        fin>>b[i];

    for (int i=na;i<na+nb;i++)
        ptr[i]=&b[i-na];

    comfract ans=0;

    int n=na+nb;
    int kol_fract=0,kol_com=0;
    for (int i=0;i<n;i++)
    {
        comfract *temp=dynamic_cast <comfract*> (ptr[i]);
        if (temp)
        {
            ans+=(*temp);
            kol_com++;
        }
        else
        {
            ans+=comfract(*ptr[i]);
            kol_fract++;
        }
    }
    cout<<"summa = "<<ans<<endl;
    cout<<"kol-vo base Fract - "<<kol_fract<<endl;
    cout<<"kol-vo proizvod comfract - "<<kol_com<<endl;
    return 0;
}
