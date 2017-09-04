#include <iostream>
#include <iomanip>

using namespace std;

extern "C" double* _fastcall func();

int main()
{
	double* ans=func();
	cout << "const ln2=" <<fixed<<setprecision(9)<< ans[0] << endl;
	cout << "solve ln2=" << fixed << setprecision(9) << ans[1] << endl;
	cout << "count:" <<  '\t' << "iter:" << endl;
	cout << 5 << '\t' << 93 << endl;
	cout << 7 << '\t' << 878 << endl;
	cout << 9 << '\t' << 32289 << endl;
	system("pause");
	return 0;
}