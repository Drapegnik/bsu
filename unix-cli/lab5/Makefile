all: sheel

CFLAGS=-Wall
LDFLAGS=
BUILD_PATH=build

clean:
	rm -rf build
	mkdir build
sheel: clean sheel.cpp utils.cpp sheel.h
	g++ ${CFLAGS} sheel.cpp utils.cpp -o ${BUILD_PATH}/sheel
run: sheel
	./${BUILD_PATH}/sheel