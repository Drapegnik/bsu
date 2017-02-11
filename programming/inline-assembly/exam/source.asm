;
; Created by Drapegnik on 19.06.15.
;
.386
.model flat
.code
_func@8 proc
		push ebp
		mov ebp, esp 
		mov eax, dword ptr [ebp+8]		; n
		mov ebx, dword ptr [ebp+12]		; a[]
		
		;xor ecx,ecx
		;mov edx,24
		;mov [ebx][ecx*4],edx

		pop ebp
		ret 8
_func@8 endp

end