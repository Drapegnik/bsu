#!/usr/bin/env bash
mpirun -np "$1" python solver.py "$2" "$3"