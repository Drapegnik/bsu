//
// Created by Drapegnik on 16.05.15.
//
#include <iostream>

using namespace std;

extern "C" int _fastcall MyLen(char*);
extern "C" int _fastcall Count(char*, int);

int main()
{
	char str[100] = "Hello  World!   asf";
	cout << Count(str, MyLen(str)) << endl;
	system("pause");
	return 0;
}