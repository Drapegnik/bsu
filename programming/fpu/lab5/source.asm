.386
.model flat
.data
res dq 10 dup (0)
x dq ?
eps dq ?
num dd 2
k dd 1
tmp dq ?

.code
_func@16 proc
		finit
		push ebp
		mov ebp, esp 
		fld qword ptr [ebp+8]
		fld qword ptr [ebp+16]
		
		lea ebx,res
		fstp eps
		fst x

		fabs
		fiadd num
		fsqrt
		fdiv x
		
		inc num		;=3
		
		fild k
		fiadd num
		fld st(0)
		fmul st(1),st(0)
		fcomp
		fdiv st(1),st(0)
		fld st(1)
		fxch
		inc num

		_while:
			fmul st(1),st(0)
			fcomp
			fild k
			fiadd num
			fld st(0)
			fmul st(1),st(0)
			fcomp

			fdiv st(1),st(0)
			inc num
			fstp tmp
			fadd st(1),st(0)
			fld st(0)
			fabs
			fcom eps
			fstsw ax
			sahf
			fstp qword ptr [ebx] ;очищение
			fld tmp
		ja _while

		fstp qword ptr [ebx]	;(k+3)^2
		fstp qword ptr [ebx]	;k-й член
		fstp qword ptr [ebx]	;сумма
		lea eax,res
		
		pop ebp
		ret 16
_func@16 endp

end
