//
// Created by Drapegnik on 02.06.15.
//
#include <iostream>

using namespace std;

extern "C" void _stdcall func(int, int*);

int main()
{
	int n;
	int a[100];
	a[0] = 1234;
	cin >> n;
	func(n, a);
	for (int i = 1; i < a[0]; i++)
		cout << a[i] << " ";
	system("pause");
	return 0;
}