//
// Created by Drapegnik on 11.11.17.
//
// wheel + shell = sheel - my own implementation of shell

#include <iostream>
#include <algorithm>
#include <unistd.h>
#include <fcntl.h>

using namespace std;

const int MAX_ARGS = 256;
enum CommandType { PIPE, REDIRECT, SIMPLE };

int read_args(char**);

void run_command(int, char**);

void run_pipe(char**, char**);

void run_redirect(char**, char**);

CommandType parse_command(int, char**, char**, char**);

string trim(string&);

bool is_exit_command(string&);
