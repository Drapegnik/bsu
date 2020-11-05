.486
.model flat, stdcall                    
option casemap :none

include windows.inc     ; always first

include masm32.inc
include gdi32.inc
include user32.inc
include kernel32.inc

includelib masm32.lib
includelib gdi32.lib
includelib user32.lib
includelib kernel32.lib

.data
    buf db  300 dup(' ')
    TAB db 10 dup(10 dup(0))
    n   dd  0
    mes1 db "puts count of elements: ",0
    mes2 db "puts elements: ",13,10,0
    space db ' ',0
    warn db "!!!!!",13,10,0
    ind dd 0
    siz1 dd 0
    siz2 dd 0
    tmp db 100 dup(0)
    flag db 0
    
.code

MainProc	proc
            invoke StdOut, addr mes1
            invoke  StdIn, addr buf, 300
            invoke  atol, addr buf
            mov n,eax
            
            invoke StdOut, addr mes2
            mov ecx,n
            xor ebx,ebx
            
            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; IN
            
            _while1:
                push ecx
                invoke  StdIn, addr buf, 300
                sub eax,2
                mov [buf+eax],0
                inc eax
                mov ecx,eax
                lea esi,buf 
                lea edi,TAB
                add edi,ebx
                cld
                rep movsb
                pop ecx
                add ebx,10
            loop _while1
            
     ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; SORT
     _GLOBALWHILE:
            mov flag,0
            mov ind,0
            ;;;;;;;;;;;;;;;;;;;;;;;;;;;; min size
            mov ecx,n
            dec ecx
            _while2:
                push ecx
                
                lea esi,TAB
                lea edi,TAB
                add esi,ind
                add edi,ind
                add edi,10
                
                xor ecx,ecx
                xor ebx,ebx
                xor edx,edx
                
                _size1:
                    inc esi
                    inc ebx
                    mov al,0
                    cmp [esi],al
                jne _size1
                mov siz1,ebx
                
                _size2:
                    inc edi
                    inc edx
                    mov al,0
                    cmp [edi],al
                jne _size2
                mov siz2,edx
                
                cmp ebx,edx
                jl _les
                    mov ecx,edx
                    jmp _next1
                _les:
                    mov ecx,ebx
                _next1:
                
                inc ecx
                
                ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; cmp
                
                lea esi,TAB
                lea edi,TAB
                add esi,ind
                add edi,ind
                add edi,10
                
                cld
                repe cmpsb
                
                ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; swap
                
                jle _met
                    mov flag,1
                    ;invoke StdOut,addr warn
                    lea esi,TAB
                    add esi,ind
                    lea edi,tmp
                    mov ecx,siz1
                    inc ecx
                    cld
                    rep movsb
                    
                    lea esi,TAB
                    add esi,ind
                    add esi,10
                    lea edi,TAB
                    add edi,ind
                    mov ecx,siz2
                    inc ecx
                    cld
                    rep movsb
                    
                    lea esi,tmp
                    lea edi,TAB
                    add edi,ind
                    add edi,10
                    mov ecx,siz1
                    inc ecx
                    cld
                    rep movsb                
                _met:
                add ind,10
                pop ecx
                dec ecx
                cmp ecx,0
            jne _while2
          cmp flag,0
     jne _GLOBALWHILE
            
            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; OUT
     
            xor ebx,ebx
            lea edi, TAB
            _while3:
                invoke StdOut, edi
                invoke StdOut, addr space
                add edi, 10
                inc ebx
                cmp ebx,n
            jne _while3
            
            invoke  StdIn, addr buf, 300
            invoke  ExitProcess, 0
MainProc    endp

end MainProc
