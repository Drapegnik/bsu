;
; Created by Drapegnik on 16.05.15.
;
.386
.model flat
.code
@MyLen@4 proc
		cld
		mov edi,ecx
		mov ecx,100
		mov al,0
	repne scasb
		mov eax,100
		sub eax,ecx
		dec eax
		
		ret
@MyLen@4 endp

@Count@8 proc
		cld
		mov edi,ecx
		mov ecx,edx
		mov al,' '
		mov [edi][ecx], al
		inc ecx
		mov al,0
		mov [edi+ecx],al
		mov al,' '
	
	repe scasb
		xor ebx,ebx
	
	beg0:
	repne scasb 
		inc ebx
	repe scasb
		test ecx,0FFFFFFFFh
		jne beg0
		mov eax,ebx
		ret
@Count@8 endp

end
