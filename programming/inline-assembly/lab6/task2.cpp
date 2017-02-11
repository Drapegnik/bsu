//
// Created by Drapegnik on 13.05.15.
//
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;
ifstream fin("task2.txt");

int main()
{
	int n, m,a[100],b[100],sum[100],mul[100];
	fin >> n;

	for (int i = 0; i < n; i++)
		fin >> a[i];

	fin >> m;
	for (int i = 0; i < m; i++)
		fin >> b[i];
	
	for (int i = 0; i < max(n, m); i++)
		sum[i] = 0;
	for (int i = 0; i < n+m; i++)
		mul[i] = 0;

	__asm
	{
		mov eax,n
		mov ebx,m
		cmp eax,ebx
		jnl _n_max
		
		_n_max:
			xor ecx,ecx
			_beg:
				mov esi, a[ecx*4]
				mov sum[ecx*4], esi
				inc ecx
				cmp ecx, eax
			jl _beg

			xor ecx,ecx
			_beg2:
				mov esi, b[ecx*4]
				add sum[ecx * 4], esi
				inc ecx
				cmp ecx, ebx
			jl _beg2
	}

	for (int i = 0; i < n; i++)
		cout << sum[i] << " ";
	system("pause");
	return 0;

}