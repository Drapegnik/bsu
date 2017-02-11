//
// Created by Drapegnik on 13.05.15.
//
#include <iostream>

using namespace std;

int main()
{

	int n,ans=0;
	cin >> n;
	__asm
	{
		bsr eax, n
		mov ans, eax
		jz _null
	}
	cout << ans+1;
	system("pause");
	return 0;

	_null:
	cout << 0;
	system("pause");
	return 0;

}