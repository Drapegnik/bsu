#!/usr/bin/env bash
#javac -d ${1:-'out/production/lab1'} src/*.java
cd ${1:-'out/production/lab1'}
rmiregistry $RMI_PORT