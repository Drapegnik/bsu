.386
.model flat
.data
res dq 100 dup (?)
otr dq 100 dup (?)
step dq 0.01
count dq 0

.code
_func@24 proc
		finit
		push ebp
		mov ebp, esp 
		fld qword ptr [ebp+8]
		fld qword ptr [ebp+16]
		fld qword ptr [ebp+24]
		
		lea ebx,res
		;fstp qword ptr [ebx]
		;fstp qword ptr [ebx+8]
		;fstp qword ptr [ebx+16]

	;	fld step
	;	fstp qword ptr [ebx]
	;	fld1
	;	fld count
	;	fadd st(0),st(1)
	;	fadd st(0),st(1)
	;	fadd st(0),st(1)
		
		fstp qword ptr [ebx+8]

		lea eax,res
		
		pop ebp
		ret 24
_func@24 endp

end
