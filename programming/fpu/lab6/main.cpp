#include <windows.h>
#include "resource.h"
#include <iostream>
#include <stdlib.h>
#include <stdio.h>

extern "C" double* _stdcall func(double);

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
			char s[100];
			GetDlgItemText(hDlg, IDC_EDIT1, s, 100);
			double x = atof(s);

			
			double* ans;
			ans = func(x);
			
			sprintf_s(s, "%f", ans[0]);
			SetDlgItemText(hDlg, IDC_EDIT2, s);
			
			sprintf_s(s, "%f", ans[1]);
			SetDlgItemText(hDlg, IDC_EDIT3, s);

			sprintf_s(s, "%f", ans[2]);
			SetDlgItemText(hDlg, IDC_EDIT4, s);
			return (INT_PTR)TRUE;
		}
		break;
	}
	return (INT_PTR)FALSE;
}