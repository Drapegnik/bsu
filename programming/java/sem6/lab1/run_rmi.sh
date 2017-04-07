#!/usr/bin/env bash
cd ${1:-'target/classes'}
rmiregistry $RMI_PORT