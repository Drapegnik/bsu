//
// Created by Drapegnik on 18.03.14.
//
#include <iostream>

using namespace std;

int n,a;

int binpow (int a, int n) {
	if (n == 0)
		return 1;
	if (n % 2 == 1)
		return binpow (a, n-1) * a;
	else {
		int b = binpow (a, n/2);
		return b * b;
	}
}

int main()
{
    cin>>a>>n;
    cout<<binpow(a,n)<<endl;

    int res = 1;
	while (n>0)
    {
		if (n%2!=0)
			res*=a;
		a*=a;
		n/=2;;
	}
	cout<<res<<endl;

    return 0;
}
