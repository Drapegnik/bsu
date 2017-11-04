#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <stdio.h>
#include "swapper.h"

int swap(char* filename1, char* filename2) {
    int file1 = 0;
    int file2 = 0;
    if ((file1 = open(filename1, O_RDWR)) < -1) {
        return 1;
    }
    if ((file2 = open(filename2, O_RDWR)) < -1) {
        return 1;
    }
    int lenght1 = lseek(file1, 0, SEEK_END);
    int lenght2 = lseek(file2, 0, SEEK_END);
    printf("file1 lenght=%d\n", lenght1);
    printf("file2 lenght=%d\n", lenght2);

    int minFile, maxFile, minLenght, maxLenght;
    if (lenght1 <= lenght2) {
        minFile = file1;
        maxFile = file2;
        minLenght = lenght1;
        maxLenght = lenght2;
    } else {
        minFile = file2;
        maxFile = file1;
        minLenght = lenght2;
        maxLenght = lenght1;
    }

    for (int i = 0; i < maxLenght; i++) {
        char buffer1[1];
        char buffer2[1];
        lseek(minFile, i, SEEK_SET);
        lseek(maxFile, i, SEEK_SET);
        if (i < minLenght) {
            read(minFile, buffer1, 1);
        }
        read(maxFile, buffer2, 1);
        lseek(minFile, i, SEEK_SET);
        lseek(maxFile, i, SEEK_SET);
        if (i < minLenght) {
            write(maxFile, buffer1, 1);
        }
        write(minFile, buffer2, 1);
    }
    ftruncate(maxFile, minLenght);
    return 0;
}
 
int main(int argc, char ** args) {
    if (argc != 3) {
        printf("Should be exactly two arguments \n");
        return 1;
    }
    return swap(args[1], args[2]);
}
