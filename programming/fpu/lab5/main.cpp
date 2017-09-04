#include <iostream>

using namespace std;

extern "C" double* _stdcall func(double,double);

int main()
{
	double eps, x;
	eps = 0.01;
	x = -2;
	//cin >> eps >> x;
	double* sum = func(x,eps);
	cout << sum[0] << endl;
	system("pause");
	return 0;
}