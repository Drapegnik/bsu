#include "sheel.h"

int read_args(char **argv) {
	int argc = 0;
	char *cstr, *token;
	string args_line, trimmed_args;

	getline(cin, args_line);

	if (args_line.empty()) {
		return 0;
	}

	trimmed_args = trim(args_line);
	if (is_exit_command(trimmed_args)) {
		cout << "bye!" << endl;
		exit(0);
	}

	cstr = new char[args_line.size() + 1];
	strcpy(cstr, args_line.c_str());

	token = strtok(cstr, " ");
	while (token != NULL) {
		argv[argc] = token;
		token = strtok(NULL, " ");
		argc++;
	}

  argv[argc] = NULL; // last argument should be NULL so that execvp works
  return argc;
}

void run_command(int argc, char** argv) {
  pid_t pid;
  pid = fork();

  if (pid < 0) {
    perror("fork failed");
  } else if (pid == 0) {
    execvp(argv[0], argv);
    perror("execvp failed");
  } else {
    waitpid(pid, NULL, 0);
  }
}

string trim(string& str) {
	int first = str.find_first_not_of(' ');
	int last = str.find_last_not_of(' ');
  return str.substr(first, (last - first + 1));
}

bool is_exit_command(string& command) {
	transform(command.begin(), command.end(), command.begin(), ::tolower);
  return (command == "q" || command == "quit" || command == "exit");
}