#include <iostream>

using namespace std;

extern "C" double* _stdcall func(double,double,double);

int main()
{
	double a, b, c;
	cin >> a >> b >> c;
	double* x=func(a, b, c);
	for (int i = 0; i < 3; i++)
		cout << x[i] << endl;
	system("pause");
	return 0;
}