#!/usr/bin/env bash
printf ' * `ping %s %s`:\n' "$2" $1
echo '```'
ping ${2:-'-c 5'} $1
echo '```'