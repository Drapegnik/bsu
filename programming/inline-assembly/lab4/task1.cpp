//
// Created by Drapegnik on 13.05.15.
//
#include <iostream>

using namespace std;

int main()
{

	int n, sum = 0, count = 0,ten = 10;
	bool f = false;
	cin >> n;
	__asm
	{
		mov eax, n
		xor edi,edi
		_while:
			cdq
			idiv ten
			add sum, edx
			test edx, 1
			jnz _next
				; ÷¸ò
				inc count
			_next:
			imul edi,ten
			add edi,edx
			cmp eax,0
		jne _while
		
		cmp edi,n
		jne _end
			mov f,1
		_end:
	}
	cout <<"sum: "<< sum << endl;
	cout <<"kol-vo chet: "<< count << endl;
	if (f)
		cout << "polinom" << endl;
	else
		cout << "ne polinom" << endl;
	system("pause");
	return 0;
}