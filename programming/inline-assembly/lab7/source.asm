;
; Created by Drapegnik on 16.05.15.
;
.386
.model flat

.data
str1 db 100 dup('0')
str2 db 100 dup('0')
str3 db 100 dup('0')
len1 dd ?
len2 dd ?

.code

_sum@8 proc
        push ebp
		mov ebp, esp 
		mov ebx, dword ptr [ebp+8]
		
		xor ecx,ecx
		_while1:
			mov dl, [ebx]
			inc ebx
			inc ecx
			cmp dl, 0
		jne _while1

		dec ecx
		dec ebx
		dec ebx

		mov len1,ecx

		lea esi,[ebx]
		lea edi,str1
		std

		_reverse1:
			lodsb
			mov byte ptr[edi],al
			inc edi
		loop _reverse1
		cld

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		mov ebx, dword ptr [ebp+12]
		xor ecx,ecx
		_while2:
			mov dl, [ebx]
			inc ebx
			inc ecx
			cmp dl, 0
		jne _while2

		dec ecx
		dec ebx
		dec ebx

		mov len2,ecx

		lea esi,[ebx]
		lea edi,str2
		std

		_reverse2:
			lodsb
			mov byte ptr[edi],al
			inc edi
		loop _reverse2
		cld
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		
		mov ecx,len1
		cmp ecx,len2
		jl _len2

		lea esi,str1
		lea edi,str2
		jmp _next

		_len2:
		lea esi,str2
		lea edi,str1
		mov ecx,len2
		
		_next:

		mov len1,ecx
		
		xor eax,eax
		_sum:
			add al,byte ptr[edi]
			sub byte ptr[esi],'0'
			add al,byte ptr[esi]
			
			sub al,'0'

			cbw
			mov bl,10
			div bl

			add ah,'0'

			
			mov byte ptr[esi],ah
			
			inc esi
			inc edi
		loop _sum

		cmp al,0
		je _next2
		add byte ptr[esi],al
		inc len1
		inc esi

		_next2:

		mov ebx,0
		mov [esi],ebx
		;sub esi,len1

		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		
		mov ecx,len1
		dec esi

		lea edi,str3
		std

		_reverse3:
			lodsb
			mov byte ptr[edi],al
			inc edi
		loop _reverse3
		cld

		mov byte ptr[edi],0
		lea eax,str3

		pop ebp
		ret 8
_sum@8 endp

end