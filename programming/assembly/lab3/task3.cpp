//
// Created by Drapegnik on 05.05.15.
//
#include <iostream>

using namespace std;


int main()
{
	int a, b, x;
	cin >> a >> b;

	__asm
	{
		mov eax, b
		neg eax
		cdq
		idiv a
		mov x, eax
	}

	cout << x << endl;
	system("pause");
	return 0;
}


