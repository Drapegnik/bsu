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
		mov eax, a
		add eax, 1
		imul eax, a
		imul eax, a
		imul eax, a
		add eax, 1
		imul eax, a
		mov rez, eax
	}
	cout << rez << endl;
	system("pause");
	return 0;
}

