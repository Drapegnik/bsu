#!/usr/bin/env bash
export RMI_PORT=${1:-2001}
export RMI_HOST=${2:-10.160.98.85}
cd ${3:-'out/production/lab1'}
java -Djava.security.policy=client.policy app/Client