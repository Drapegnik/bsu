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
    zero db "0",0
    one db "1",0
    buf db  200 dup('0')
    bit BYTE  10000000b
.code

MainProc	proc
            invoke  StdIn,addr buf,200
            invoke  StripLF, addr buf
            invoke  atol, addr buf
            
            mov ebx,eax
            _while:
                test bl,bit
                jz _zero
                    invoke  StdOut,addr one
                    jmp _next
                 _zero:
                   invoke  StdOut,addr zero
                _next:
                
                shr bit,1
                cmp bit,0
            jnz _while
            
            invoke  StdIn, addr buf,200
            invoke  ExitProcess, 0
MainProc    endp

end MainProc
