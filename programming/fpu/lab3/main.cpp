#include <iostream>
#include <iomanip>

using namespace std;

extern "C" double* _fastcall func();

int main()
{
	double* ans = func();
	cout << "const integral=" << 82.683 << endl;
	cout << "solve integral=" << ans[0] << endl;
	system("pause");
	return 0;
}