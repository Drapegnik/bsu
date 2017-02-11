;
; Created by Drapegnik on 02.06.15.
;
.386
.model flat
.code
_func@8 proc
		push ebp
		mov ebp, esp 
		mov edi, dword ptr [ebp+8]
		mov ebx, dword ptr [ebp+12]
		
		mov ecx,1
		mov esi,2
		
		mov eax,edi
		
		_do:
			cdq
			idiv esi
			cmp edx,0
			jnz _notdiv
		
			mov [ebx][ecx*4],esi	
			inc ecx		
			
			_while:
				cdq
				idiv esi
				cmp edx,0
			jz _while 

			_notdiv:
				imul eax,esi
				add eax,edx
				cmp esi,3
				jl _inc
					inc esi
				_inc:
					inc esi

			
			cmp esi,edi
			jg _end
					
			cmp eax,0
		jnz _do

		_end:

		mov [ebx][0],ecx
		pop ebp
		ret 8
_func@8 endp

end
