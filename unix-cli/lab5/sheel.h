//
// Created by Drapegnik on 11.11.17.
//
// wheel + shell = sheel - my own implementation of shell

#include <iostream>
#include <algorithm>
#include <unistd.h>

using namespace std;

const int MAX_ARGS = 256;

int read_args(char**);

void run_command(int, char**);

string trim(string&);

bool is_exit_command(string&);
