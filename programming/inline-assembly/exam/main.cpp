//
// Created by Drapegnik on 19.06.15.
//
#include <windows.h>
#include "resource.h"
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
char buf[100];

extern "C" void _stdcall func(int, int*);

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
			int a[100];
			a[0] = 1234;
			a[1] = 133;
			a[2] = 71234;
			func(n, a);
			string s;
			for (int i = 2; i>=0; i--)
			{
				s.push_back(' ');
			//	s.push_back(',');
				while (a[i]>0)
				{
					s.push_back('0'+(a[i] % 10));
					a[i] /= 10;
				}	
			}
			
			for (int i = 0; i < s.length(); i++)
				buf[i] = s[s.length() - 1 - i];

			SetDlgItemText(hDlg, IDC_EDIT2, buf);
			return (INT_PTR)TRUE;
		}
		break;
	}
	return (INT_PTR)FALSE;
}