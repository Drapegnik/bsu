//
// Created by Drapegnik on 05.05.15.
//
#include <iostream>

using namespace std;

int main()
{
	int a, ans = 0;
	cin >> a;
	__asm
	{
		mov eax, a
		cmp eax, 1
		je odyn
		my_while :
			inc ans
			imul eax, a
			jno my_while
	}
	cout << ans << endl;
	system("pause");
	return 0;
odyn:
	{
		cout << "infinity" << endl;
		system("pause");
		return 0;
	}

}