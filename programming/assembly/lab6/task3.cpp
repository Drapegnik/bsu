//
// Created by Drapegnik on 03.06.15.
//
#include <iostream>

using namespace std;

int main()
{
	int n, m, a[100], b[100], found;
	cout << "length of the first array: ";
	cin >> n;
	cout << "first array: ";
	for (int i = 0; i<n; i++)
		cin >> a[i];
	cout << "length of the second array: ";
	cin >> m;
	cout << "second array: ";
	for (int i = 0; i<m; i++)
		cin >> b[i];
	__asm
	{
		xor ebx, ebx
			dec ebx
		rep1 :
		inc ebx
			mov found, 0
			mov edx, a[ebx * 4]
			jmp findinsec
		cont1 :
		cmp found, 0
			je cont2
			jmp rem1 // dec ebx in remove	
		cont2 :
		inc ebx
			cmp ebx, n
			je fin
			dec ebx
			jmp rep1

		findinsec :
		mov ecx, m
			cmp ecx, 0
			je cont1
		rep2 :
		dec ecx
			mov eax, b[ecx * 4]
			inc ecx
			cmp eax, edx
			jne endloop
			mov found, 1
		endloop:
		loop rep2
			jmp cont1

		rem1 : // remove element on ebx position
		mov ecx, n
			mov edx, ebx
		rep3 :
		inc edx
			mov eax, a[edx * 4]
			dec edx
			mov a[edx * 4], eax
			inc edx
			cmp edx, n
			jne rep3

			dec ebx
			dec n
			jmp cont2

		fin :
	}
	cout << "first array without elements of the second: ";
	if (n == 0)
		cout << "empty" << endl;
	else
	{
		for (int i = 0; i<n; i++)
			cout << a[i] << " ";
		cout << endl;
	}
	system("pause");
	return 0;
}