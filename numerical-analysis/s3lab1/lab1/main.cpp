//
//  main.cpp
//  lab1
//
//  Created by Ivan Pazhitnykh on 18.10.15.
//  Copyright © 2015 Ivan Pazhitnykh. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <math.h>
#include <limits.h>
#include <vector>
#include <iomanip>
using namespace std;

ifstream fin ("input.txt");
ofstream fout ("output.txt");

int gauss (vector < vector<double> > a, vector < vector<double> > &e, vector<double> &ans, double &det)
{
    const double EPS=0.000000000001;            //эквивалент нуля
    const double INF=INT_MAX;                   //эквивалент бесконечности
    int n = (int) a.size();
    int m = (int) a[0].size() - 1;
    int ins=0;
    
    vector<int> where (m, -1);                              //где будет ответ
    
    for (int col=0, row=0; col<m && row<n; col++)
    {
        int sel = row;
        
        for (int i=row; i<n; i++)                           //выбирает главный по столбцу
            if (fabs (a[i][col]) > fabs (a[sel][col]))
                sel = i;
        
        if (fabs (a[sel][col]) < EPS)                       //проверка на равенство нулю
            continue;
        
        for (int i=col; i<=m; i++)                          //перестановка строк
        {
            swap (a[sel][i], a[row][i]);
            swap (e[sel][i], e[row][i]);
        }
        
        ins++;                                              //инкрементируем кол-во перестановок
        where[col] = row;                                   //сохраняем изменеия индексов
        
        for (int i=0; i<n; i++)                             //прямой ход
            if (i != row)
            {
                double c = a[i][col] / a[row][col];
                for (int j=0; j<=m; j++)
                {
                    a[i][j] -= a[row][j] * c;               //исключение переменных
                    e[i][j] -= e[row][j] * c;
                }
            }
        row++;
    }
    
    for (int col=0, row=0; col<m; col++)                          //обратный ход
    {
        for (int i=0; i<n; i++)
            if (i != row)
            {
                double c = a[i][col]/a[row][col];
                //a[i][col] -= a[row][col] * c;
                e[i][col] -= e[row][col] * c;
            }
        row++;
    }
    
    ans.assign (m, 0);
    for (int i=0; i<m; i++)                                     //получаем ответ
        if (where[i] != -1)
            ans[i] = a[where[i]][m] / a[where[i]][i];
    
    for (int row=0; row<n; row++)                               //находим обратную
        for (int col=0; col<m; col++)
           e[row][col]/=a[where[row]][row];
    
    det=1;                                                  //вычисляем определитель
    for (int i=0; i<n; i++)
        det*=a[i][i];
    if (!ins%2)
        det*=(-1);
        
    for (int i=0; i<m; ++i)
        if (where[i] == -1)
            return INF;
    return 1;
}

int main()
{
    int n,m;
    fin>>n>>m;
    
    vector< vector<double> > a(n, vector<double> (m+1,0));
    vector< vector<double> > e(n, vector<double> (m+1,0));
    vector< vector<double> > R(n, vector<double> (m+1,0));
    vector <double> ans (m,0);
    vector <double> r (m,0);
    double det=1;
    
    for (int i=0;i<n;i++)
        e[i][i]=1;
    
    for (int i=0;i<n;i++)
        for (int j=0;j<m+1;j++)
            fin>>a[i][j];
    
    fout<<"answer - ";
    if (gauss(a, e, ans, det)==1)
    {
        for (int i=0;i<m;i++)
            fout<<ans[i]<<" ";
        fout<<endl<<endl;
        fout<<"det - "<<det<<endl<<endl;
        
        for (int i=0; i<m; i++)             //находим вектор невязки
        {
            for (int j=0;j<m;j++)
                r[i]+=ans[j]*a[i][j];
            r[i]=fabs(fabs(r[i])-fabs(a[i][m]));
        }
        
        
        for (int i=0; i<n; i++)                 //находим матрицу невязки
            for (int j=0; j<n; j++)
                for (int k=0; k<n; k++)
                    R[i][j]+=a[i][k]*e[k][j];
        
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                if (i==j)
                    R[i][j]=fabs(R[i][j]);
        
        for (int i=0; i<n; i++)
            R[i][i]=fabs(R[i][i]-1);
        
        fout<<"r - ";
        for (int i=0;i<m;i++)
            fout<<r[i]<<" ";
        fout<<endl<<endl;
    }
    
    double normA=0,normE=0,normR=0,normr=0;
    for (int i=0;i<n;i++)                   //находим нормы и число обусловленности
    {
        double sum=0;
        for (int j=0; j<m; j++)
            sum+=a[i][j];
        normA=max(normA,sum);
    }
    for (int i=0;i<n;i++)
    {
        double sum=0;
        for (int j=0; j<m; j++)
            sum+=e[i][j];
        normE=max(normE,sum);
    }
    for (int i=0;i<n;i++)
    {
        double sum=0;
        for (int j=0; j<m; j++)
            sum+=R[i][j];
        normR=max(normR,sum);
    }
    for (int i=0;i<n;i++)
        normr+=fabs(r[i]);
    
    fout<<"condition number - "<<normA*normE<<endl<<endl;
    
    fout<<"inverse matrix:"<<endl;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
            fout<<e[i][j]<<"\t";
        fout<<endl;
    }
    
    fout<<endl<<"R:"<<endl;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
            fout<<R[i][j]<<"\t";
        fout<<endl;
    }
    
    fout<<endl<<"norma R - "<<normR<<endl;
    fout<<"norma r - "<<normr<<endl;
    
    return 0;
}
