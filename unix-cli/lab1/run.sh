#!/usr/bin/env bash

gcc -Wall -ggdb hello.c -o hello
echo --------------------------
echo '# without args:'
./hello
echo --------------------------

echo '# with bash args:'
./hello 'im form bash script'
echo --------------------------

echo '# with cli args:'
./hello "$*"
echo --------------------------