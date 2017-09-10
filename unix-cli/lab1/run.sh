gcc -Wall -ggdb hello.c -o hello.o
echo --------------------------
echo '# without args:'
./hello.o
echo --------------------------

echo '# with bash args:'
./hello.o 'im form bash script'
echo --------------------------

echo '# with cli args:'
./hello.o "$*"
echo --------------------------