#include<stdio.h>

int main(int argc, char *argv[]) {
	printf("-> Hello World!\n");
	if (argc < 2) {
		printf("-> There's no arguments!\n");
		return 0;
	}

	printf("-> Args: %s\n", argv[1]);
	return 0;
}
