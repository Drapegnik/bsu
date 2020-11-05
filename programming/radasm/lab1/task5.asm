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
    buf db  300 dup(' '),0
    curpos dd  0
    ans dd 0
.code

check proc
    mov ebx,curpos
    _loop:
        cmp [buf+ebx],48
        jl _end1
        cmp [buf+ebx],57
        jg _end2
        inc ebx
    jmp _loop
        
        _end1:
            cmp [buf+ebx],32
            jne _end3
               inc ans
               jmp _END
        _end2:
        _end3:
            _while2:
                inc ebx
                cmp [buf+ebx],32
            jne _while2
        _END:
    mov curpos,ebx
    ret
check endp

MainProc	proc
            invoke  StdIn, addr buf, 300
            sub eax, 2
            mov [buf+eax],' '
            inc eax
            mov [buf+eax],0
            
            xor ebx,ebx
            
            _while:
                cmp [buf+ebx],32
                jne _next1
                    inc ebx
                    jmp _next2
                _next1:
                    mov curpos,ebx
                    call check
                    mov ebx,curpos
                _next2:
                cmp [buf+ebx],0
            jnz _while
            
            mov eax,ans
            
            invoke ltoa,eax, addr buf
            invoke StdOut, addr buf
            
            invoke  StdIn, addr buf, 300
            invoke  ExitProcess, 0
MainProc    endp

end MainProc
