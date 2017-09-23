#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
   int fd = open("lala.txt", O_WRONLY|O_CREAT);
   write(fd, "Lol\n", 4);
   return 0;
}
