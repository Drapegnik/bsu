//
// Created by Drapegnik on 30.11.14.
//
#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

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
        friend void operator += (Fraction&, Fraction&);
        friend istream& operator >> (istream& os, Fraction& obj);
        friend ostream& operator << (ostream& os, const Fraction& obj);
};

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

Fraction operator * (Fraction f1, Fraction f2)
{
    long long temp;
    int num1=0,num2=0;
    temp=fabs(f1.fract);
    while (temp>0)
    {
        temp/=10;
        num1++;
    }
    temp=fabs(f2.fract);
    while (temp>0)
    {
        temp/=10;
        num2++;
    }

    long long temp1=f1.intp;
    for (int i=0;i<num1;i++)
        temp1*=10;
    if (f1.intp<0)
        f1.fract*=(-1);
    temp1+=f1.fract;

    long long temp2=f2.intp;
    for (int i=0;i<num2;i++)
        temp2*=10;
    if (f2.intp<0)
        f2.fract*=(-1);
    temp2+=f2.fract;

    temp=temp1*temp2;



    long long osn=1;
    int sz=num1+num2;

    while (sz>9)
    {
        temp/=10;
        sz--;
    }

    for (int i=0;i<sz;i++)
        osn*=10;
    Fraction ans(temp/osn,temp%osn);
    if (ans.intp!=0)
        ans.fract=fabs(ans.fract);
    return ans;
}

void operator += (Fraction& f1, Fraction& f2)
{
    f1=f1+f2;
}

istream& operator >> (istream& os, Fraction& obj)
{
    double a;  //чтение как double
    os>>a;
    obj=a;
    //os>>obj.intp>>obj.fract;  // - вот так через int'ы
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

int main()
{
    Fraction p[100];
    int n=0;
    cout<<"kol-vo elementov:"<<endl;
    cin>>n;
    cout<<"vvedite elemenry v vide x.y"<<endl;

    for (int i=0;i<n;i++)
        cin>>p[i];

    for (int i=0;i<n;i++)
        for (int j=i+1;j<n;j++)
            if (p[i]>=p[j])
                swap(p[i],p[j]);

    Fraction ans=0;

    for (int i=0;i<n;i++)
        {
            ans+=p[i];
            cout<<p[i]<<" ";
        }
    cout<<endl<<"summa elementov mas = "<<ans<<endl;
    Fraction a,b;
    cout<<"vvedite a i b"<<endl;
    cin>>a;
    cin>>b;
    cout<<a<<" + "<<b<<" = "<<a+b<<endl;
    cout<<a<<" - "<<b<<" = "<<a-b<<endl;
    cout<<a<<" * "<<b<<" = "<<a*b<<endl;
    return 0;
}