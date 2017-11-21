all: hello

PROFILE=debug

CFLAGS-debug=-Wall
CFLAGS-debug+=-ggdb
CFLAGS-debug+=-DDEBUG=1
CFLAGS-release=-O3
CFLAGS-release+=-DNDEBUG=1g
CFLAGS=${CFLAGS-${PROFILE}}

LDFLAGS=

hello: hello.c
	gcc ${CFLAGS} hello.c -o hello
run: hello
	./hello