#!/usr/bin/env bash
export RMI_PORT=${1:-2001}
export RMI_HOST=${2:-localhost}
cd ${3:-'target/classes'}
java -Djava.security.policy=client.policy app/Client