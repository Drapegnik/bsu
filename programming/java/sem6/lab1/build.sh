#!/usr/bin/env bash
find src -name "*.java" > sources.txt
javac @sources.txt -d ${1:-'out/production/lab1'}