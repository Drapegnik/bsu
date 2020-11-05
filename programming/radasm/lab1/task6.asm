.486
.model flat, stdcall 
option casemap :none

include windows.inc ; always first

include masm32.inc
include gdi32.inc
include user32.inc
include kernel32.inc

includelib masm32.lib
includelib gdi32.lib
includelib user32.lib
includelib kernel32.lib

.data
buf db 300 dup(?)
space db 300 dup(0)

.code

MainProc proc
    invoke StdIn, addr buf, 300
    xor ebx,ebx
    lea ebx,buf
    sub eax,3
    
    _while1:
        mov cl,' '
        cmp [ebx+eax],cl
        jne _next
        dec eax
    jmp _while1
        
    _next:
    
    mov ecx,79
    sub ecx,eax
    lea ebx,space
    
    _while2:
        mov al,' '
        mov [ebx],al
        inc ebx
    loop _while2

    invoke StdOut, addr space
    invoke StdOut, addr buf
    invoke StdIn, addr buf, 300

    invoke ExitProcess, 0
MainProc endp

end MainProc