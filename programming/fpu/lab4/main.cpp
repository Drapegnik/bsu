#include <iostream>
#include <iomanip>

using namespace std;

extern "C" double* _stdcall func(double);

int main()
{
	double x;
	cin >> x;
	double* ans = func(x);

	cout << "10^" << x << "=" << fixed << setprecision(4) << ans[0] << endl;
	system("pause");
	return 0;
}