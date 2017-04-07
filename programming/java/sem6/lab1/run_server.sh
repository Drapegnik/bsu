#!/usr/bin/env bash
export DB_TYPE=${1:-sql}
export RMI_PORT=${2:-2001}
export RMI_HOST=${3}
cd ${4:-'target/classes'}
java -Djava.security.policy=server.policy app/Server