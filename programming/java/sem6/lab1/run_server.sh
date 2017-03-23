#!/usr/bin/env bash
export RMI_PORT=${1:-2001}
export RMI_HOST=${2:-localhost}
cd ${3:-'out/production/lab1'}
java -Djava.security.policy=server.policy app/Server