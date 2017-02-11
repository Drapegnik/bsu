//
// Created by Drapegnik on 02.05.15.
//
#include <windows.h>
#include "resource.h"
#include <iostream>

char buf[100];

int countnum(int a)
{
	int ans=0, ten = 10;
	_asm
	{
		mov eax,a
		_while:
			inc ans
			cdq
			idiv ten
			cmp eax,0
		jne _while
	}
	return ans;
}
void inhex(int a)
{
	char hex[17] = "0123456789ABCDEF";
	_asm
	{
		mov eax, a
		xor ecx, ecx

		_while1 :
			shr eax, 4
			inc ecx
			cmp eax, 0
			jnz _while1

		mov buf[ecx], '\0'
		dec ecx
		mov eax, a

		_while2 :
			mov ebx, 15
			and ebx, eax
			mov dl, hex[ebx]
			mov buf[ecx], dl
			dec ecx
			shr eax, 4
			cmp eax, 0
			jnz _while2
	}
}

void inbin(int a)
{
	char bin[3] = "01";
	_asm
	{
		mov eax,a
		xor ecx,ecx
		
		_while1 :
			shr eax, 1
			inc ecx
			cmp eax, 0
			jnz _while1
		
			mov buf[ecx], '\0'
		dec ecx
		mov eax,a

		_while2:
			mov ebx, 1
			and ebx, eax
			mov dl, bin[ebx]
			mov buf[ecx], dl
			dec ecx //?
			shr eax,1
			cmp eax, 0
			jnz _while2

		
	}
}

INT_PTR CALLBACK DlgProc(HWND, UINT, WPARAM, LPARAM);

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE, LPTSTR, int)
{
	DialogBox(hInstance, MAKEINTRESOURCE(IDD_DIALOG1), NULL, DlgProc);
	return 0;
}

INT_PTR CALLBACK DlgProc(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
	switch (message)
	{
	case WM_INITDIALOG:
		return (INT_PTR)TRUE;

	case WM_COMMAND:
		if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
		{
			EndDialog(hDlg, LOWORD(wParam));
			return (INT_PTR)TRUE;
		}
		if (LOWORD(wParam) == IDC_BUTTON1)
		{
			int n = GetDlgItemInt(hDlg, IDC_EDIT1, NULL, TRUE);
			SetDlgItemInt(hDlg, IDC_EDIT2, countnum(n), TRUE);
			inhex(n);
			SetDlgItemText(hDlg, IDC_EDIT3, buf);
			inbin(n);
			SetDlgItemText(hDlg, IDC_EDIT4, buf);
			return (INT_PTR)TRUE;
		}
		break;
	}
	return (INT_PTR)FALSE;
}