.386
.model flat
.data
res dq 10 dup (0)
ten dq 10.0

.code
_func@8 proc
		finit
		push ebp
		mov ebp, esp 
		
		fldl2t
		fld qword ptr [ebp+8]
		fmul st(1),st(0)

		lea ebx,res
		fstp qword ptr [ebx]

		fld st(0)
		frndint 
		fsub st(1),st(0)
		

		
		fld1
		fscale
		fxch
		fxch st(2)
		f2xm1
		fld1
		fadd
		fmul st(0),st(1)
		fstp qword ptr [ebx]
		pop ebp
		lea eax,res
		ret 8
_func@8 endp
end
