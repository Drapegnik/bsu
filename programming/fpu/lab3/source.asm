.386
.model flat
.data
res dq 10 dup (0)
count dd 1000
two dd 2
step dq ?
x dq ?

.code
@func@0 proc
		finit
		
		lea ebx,res
		
		fldpi
		fimul two
		fidiv count
		fst step

		mov ecx,count
		dec ecx
		fldz
		
		fst x
		fcos			
		fadd qword ptr [ebx]
		fstp qword ptr [ebx]
		
		fld x
		fmul x
		fadd qword ptr [ebx]
		fstp qword ptr [ebx]
		
		_for:
			fld st(0)
			fst x
			fcos		
			fimul two	
			fadd qword ptr [ebx]
			fstp qword ptr [ebx]
		
			fld x
			fmul x
			fimul two	
			fadd qword ptr [ebx]
			fstp qword ptr [ebx]
			fadd step
		loop _for
		
		fst x
		fcos			
		fadd qword ptr [ebx]
		fstp qword ptr [ebx]
		
		fld x
		fmul x
		fadd qword ptr [ebx]

		fidiv two
		fmul step

		fstp qword ptr [ebx]

		lea eax,res
		ret 
@func@0 endp
end