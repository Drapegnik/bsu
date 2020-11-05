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
    buf db 300 dup(' ')

    szCh db 0,0
    endl db 13,10,0

    count1 dd 0
    count2 dd 0

.code

MainProc	proc

            mov count1,0
            mov count2,255

            _for2:
                invoke StdOut, addr szCh
                inc [szCh]

                inc count1
                cmp count1,10
                jne _next
                    invoke StdOut, addr endl
                    mov count1,0
                _next:

                dec count2
                cmp count2,0
            jnz _for2

            invoke StdOut, addr endl

            invoke StdIn, addr buf, 30
            invoke ExitProcess, 0
MainProc    endp

end MainProc
