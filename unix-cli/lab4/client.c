#include <stdio.h>
#include "swapper.h"

int main(int argc, char ** args) {
  if (argc != 3) {
  	printf("Should be exactly two arguments \n");
    return 1;
  }
  return swap(args[1], args[2]);
}
