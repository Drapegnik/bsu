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
    buf db  300 dup('0')
    n   dd  ?
    m   dd  ?
    mes1 db "n=",0
    mes2 db "m=",0
    mes3 db 13,10,"puts elements:",13,10,0
    space db ' ',0
    
    sum dd 10 dup (0)
    endl db 13,10,0
    ind dd 0
    

.code

MainProc	proc

            invoke  StdOut, addr mes1
            invoke  StdIn, addr buf, 300
            invoke  atol, addr buf
            mov n,eax
            invoke  StdOut, addr mes2
            invoke  StdIn, addr buf, 300
            invoke  atol, addr buf
            mov m,eax
            invoke  StdOut, addr mes3
            
            mov ebx,0
            
            mov eax,n
            mul m
            mov ecx,eax
            
            
            _while:
                push ecx
                invoke  StdIn, addr buf, 300
                invoke  atol, addr buf
                pop ecx
                
                add [sum+ebx],eax
                
                inc ind
                mov eax,m
                cmp ind,eax
                jne _next
                    mov ind,0
                    add ebx,4
                _next:
            loop _while
            
            mov ecx,n
            
            xor ebx,ebx
            _out:
                push ecx
                invoke ltoa,[sum+ebx],addr buf 
                invoke StdOut, addr buf
                invoke StdOut, addr space
                add ebx,4
                pop ecx
            loop _out
            
            invoke  StdIn, addr buf, 300
            invoke  ExitProcess, 0
MainProc    endp

end MainProc
