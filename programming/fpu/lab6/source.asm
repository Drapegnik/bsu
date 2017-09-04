.386
.model flat
.data
res dq 10 dup (?)

.code
_func@8 proc
		finit
		push ebp
		mov ebp, esp 
		fld qword ptr [ebp+8]
		
		lea ebx,res
		
		fld1
		fadd st(0),st(1)
		fstp qword ptr [ebx]
		
		fld st(0)
		fsin
		fstp qword ptr [ebx+8]

		fld1
		fxch
		fyl2x
		fstp qword ptr [ebx+16]

		lea eax,res
		
		pop ebp
		ret 8
_func@8 endp

end
