all: client

BUILD_PATH=build

clean:
	rm -rf ${BUILD_PATH}
	mkdir ${BUILD_PATH}
swapper: clean swapper.c
	gcc -fPIC swapper.c -c -o ${BUILD_PATH}/swapper.o
	gcc -shared ${BUILD_PATH}/swapper.o -o ${BUILD_PATH}/libswapper.dylib
client: swapper client.c
	gcc client.c -c -o ${BUILD_PATH}/client.o
	gcc ${BUILD_PATH}/client.o -L${BUILD_PATH} -lswapper -o ${BUILD_PATH}/client
run: client file1.txt file2.txt
	./${BUILD_PATH}/client file1.txt file2.txt