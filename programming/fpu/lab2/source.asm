.386
.model flat
.data
res dq 10 dup (0)
k dq 1.0
four dq 4.0
count dd 32289

.code
@func@0 proc
		finit
		
		lea ebx,res
		fldln2
		fstp qword ptr [ebx]

		mov ecx,count
		_for:
			fld k
			fmul k
			fmul k
			fmul four
			fsub k
			fld1
			fdiv st(0),st(1)

			fld qword ptr [ebx+8]
			fadd st(0),st(1)
			fstp qword ptr [ebx+8]
			fcompp

			fld1
			fld k
			fadd st(0),st(1)
			fst k
			fcompp
		loop _for

		fld1
		fld qword ptr [ebx+8]
		fadd st(0),st(1)
		fld1
		fadd st(0),st(2)
		fdiv st(1),st(0)
		fstp qword ptr [ebx+8]
		fstp qword ptr [ebx+8]
		fcomp

		lea eax,res
		ret 
@func@0 endp
end
