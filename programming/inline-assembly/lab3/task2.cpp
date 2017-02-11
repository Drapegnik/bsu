//
// Created by Drapegnik on 05.05.15.
//
#include <iostream>

using namespace std;

int main()
{
	int a, rez;
	cin >> a;
	__asm
	{
		mov ebx, a
		sub ebx, 4
		jz	div_nul
		mov eax, a
		imul eax
		imul eax
		sub eax, 2
		cdq
		idiv ebx
		mov rez, eax

	}
	cout << rez << endl;
	system("pause");
	return 0;

div_nul:
	{
		cout << "error" << endl;
		system("pause");
		return 0;
	}
}

