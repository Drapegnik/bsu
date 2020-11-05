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
    buf     db  300 dup(?)
    res     db  20 dup('a')

.code

MainProc	proc
            invoke  StdIn, addr buf, 300
            xor ecx,ecx
            xor eax,eax
            
            _while1:
                cmp [buf+eax],'a'
                jne _next1
                    inc ecx
                _next1:
                inc eax
                cmp [buf+eax],0
            jne _while1
            
            xor eax,eax
            
            _while2:
                cmp [buf+eax],'b'
                jne _next2
                    inc [res+ecx]
                    inc ecx
                _next2:
                inc eax
                cmp [buf+eax],0
            jne _while2
            
            xor eax,eax
            
            _while3:
                cmp [buf+eax],'c'
                jne _next3
                    inc [res+ecx]
                    inc [res+ecx]
                    inc ecx
                _next3:
                inc eax
                cmp [buf+eax],0
            jne _while3
            
            mov [res+ecx],0
           
            invoke  StdOut, addr res
            invoke  StdIn, addr buf, 300
            invoke  ExitProcess, 0
MainProc    endp

end MainProc
