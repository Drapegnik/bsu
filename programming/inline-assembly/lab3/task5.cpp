//
// Created by Drapegnik on 05.05.15.
//
#include <iostream>

using namespace std;

int main()
{
	int ans = 0;
	__asm
	{
		mov eax, 50
		cdq
		mov ebx, 3
		idiv ebx
		mov ans, eax
	}
	cout << ans << endl;
	int *x, *y;
	x = new int[ans + 1];
	y = new int[ans + 1];
	__asm
	{
		mov ecx, ans
		mov esi, x
		mov edi, y

		m :
		mov eax, ecx; ecx - y / 2
			mov ebx, 3
			imul ebx; 3 * y / 2

			mov dword ptr[esi], 50; x = 50
			sub dword ptr[esi], eax; x = 50 - y / 3 * y / 2
			add esi, 4

			mov eax, ecx
			mov edx, 2
			imul edx
			mov dword ptr[edi], eax; y = ecx * 2
			add edi, 4
			loop m
	}
	for (int i = 0; i<ans; i++)
		cout << x[i] << " " << y[i] << endl;
	system("pause");
	return 0;

}