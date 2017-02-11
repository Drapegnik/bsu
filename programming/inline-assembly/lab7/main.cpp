//
// Created by Drapegnik on 16.05.15.
//
#include <windows.h>
#include "resource.h"

extern "C" char* _stdcall sum(char*, char*);

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
			char s[100], l[100];
			GetDlgItemText(hDlg, IDC_EDIT1, s, 100);
			GetDlgItemText(hDlg, IDC_EDIT2, l, 100);
			SetDlgItemText(hDlg, IDC_EDIT3, sum(s, l));
			return (INT_PTR)TRUE;
		}
		break;
	}
	return (INT_PTR)FALSE;
}