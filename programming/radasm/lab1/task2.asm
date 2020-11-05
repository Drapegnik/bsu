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
    szHelloWorld        db  "input:",9,0
    szByeWorld          db  "output:",9,0
    endl                db 13,10,0
    buf                 db  300 dup(?),

.code

MainProc	proc
            invoke  StdOut, addr szHelloWorld
            invoke  StdIn, addr buf, 300
            invoke  StdOut, addr szByeWorld
            
            xor ecx,ecx
            _while:
                cmp [buf+ecx],97
                jl _next
                    cmp [buf+ecx],122
                    jg _next
                        sub [buf+ecx],32
                _next:
                inc ecx
                cmp [buf+ecx],0
            jnz _while
            
            invoke  StdOut, addr buf
            invoke  StdIn, addr buf, 300
            
            invoke  ExitProcess, 0
MainProc    endp

end MainProc
