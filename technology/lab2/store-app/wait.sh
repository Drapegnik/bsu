#!/usr/bin/env bash
echo -n 'wait for localhost:'
echo ${1}

# wait for port to be listening connections
while ! nc -z 127.0.0.1 ${1}; do sleep 1; done

# open browser
open http://localhost:${1}
