//
// Created by Drapegnik on 02.05.15.
//
#include <windows.h>
#include "resource.h"
#include <iostream>
#define IDC(n) IDC_BUTTON##n

char buf[100];

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
		{
			for (int i = 0; i < 15; i++)
				for (int j = 0; j < 15; j++)
				{
					int n = i * 15 + j;
					inhex((i+1)*(j+1));
					SetDlgItemText(hDlg, IDC(1 + n), buf);
				}
			
			
			return (INT_PTR)TRUE;
		}
	

	case WM_COMMAND:
		if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
		{
			EndDialog(hDlg, LOWORD(wParam));
			return (INT_PTR)TRUE;
		}
		for (int i = 0; i < 15; i++)
			for (int j = 0; j < 15; j++)
			{
				int n = i * 15 + j;
				if (LOWORD(wParam) == IDC(1 + n))
				{
					HFONT hFont;
					HDC hdc = GetDC(hDlg);
				
					hFont = CreateFont(35, 0, 0, 0, FW_DONTCARE, FALSE, TRUE, FALSE, DEFAULT_CHARSET,
					OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY,
					DEFAULT_PITCH | FF_SWISS, "Arial");
					


					inhex(1+15 * i);
					SendMessage(GetDlgItem(hDlg,IDC(1 + 15 * i)), WM_SETFONT, WPARAM(hFont), TRUE);
					SetDlgItemText(hDlg, IDC(1 + 15*i), buf);

					inhex(1+j);
					SendMessage(GetDlgItem(hDlg, IDC(1 + j)), WM_SETFONT, WPARAM(hFont), TRUE);
					SetDlgItemText(hDlg, IDC(1 + j), buf);

					//DeleteObject(SelectObject(hdc, hFontOld));
					return (INT_PTR)TRUE;
				}
			}
		break;
	}
	return (INT_PTR)FALSE;
}