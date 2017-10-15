#!/usr/bin/env bash

cmake --build build/  --target lab1 -- -j 4

printf '' > output.txt

for n in 450 1500
    do
        echo $n 5 >> output.txt
        for r in 1 25 50 75 150
            do
                ./build/lab1 -n $n -m $n -r $r
            done
    done