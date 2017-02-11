//
// Created by Drapegnik on 13.05.15.
//
#include <iostream>

using namespace std;

int main()
{
	int n, x, l ,r, ans;
	int a[100];
	cin >> n >> x;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	l = 0;
	r = n - 1;
	__asm
	{
		mov ebx, l
		mov ecx, r
		mov edx, x
		_while:
			mov eax, ecx
			sub eax, ebx
			shr eax, 1
			
			add eax,ebx
			cmp edx, a[eax * 4]
			je _end
			jl _less
			jg _greater

			_less:
				sub eax, 1
				mov ecx, eax
				jmp _next

			_greater:
				add eax,1
				mov ebx, eax
		
		_next:
		cmp ebx,ecx
		jl _while
		

		_end:
			mov ans, eax
	}
	if (a[ans] == x)
		cout << ans + 1 << endl;
	else
		cout << -1 << " " << ans+1 << endl;
	system("pause");
	return 0;

}