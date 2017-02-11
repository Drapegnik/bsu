//
// Created by Drapegnik on 13.05.15.
//
#include <iostream>

using namespace std;

int main()
{

	int a, b, gcd;
	cin >> a >> b;
	__asm
	{
		cmp a,0
		je _end

		mov eax,a
		mov ebx,b
		
		cmp eax,ebx
		jg _next2
			xchg eax, ebx
		_next2:

		_while:
			cdq
			idiv ebx
			xchg eax,ebx
			cmp edx,0
		jne _while
			
		mov gcd,eax

		mov eax,a
		cdq
		idiv gcd
		mov a,eax
		mov eax,b
		cdq
		idiv gcd
		mov b, eax
	}
	cout << a <<"/"<<b<< endl;
	system("pause");
	return 0;

	_end:
	cout << 0 << endl;
	system("pause");
	return 0;

}