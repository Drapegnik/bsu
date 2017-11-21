#include "sheel.h"

int read_args(char **argv) {
	int argc = 0;
	string args_line;

	if (!getline(cin, args_line)) {
		cout << endl;
		exit(0);
	}

	if (args_line.empty()) {
		return 0;
	}

	string trimmed_args = trim(args_line);
	if (is_exit_command(trimmed_args)) {
		cout << "bye!" << endl;
		exit(0);
	}

	char* cstr = new char[args_line.size() + 1];
	strcpy(cstr, args_line.c_str());

	char* token = strtok(cstr, " ");
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

void run_pipe(char** cmd1, char** cmd2) {
	int descriptors[2];
  pid_t pid;
  pipe(descriptors);

  if (fork() == 0) {
    dup2(descriptors[0], 0);
    close(descriptors[1]);

    execvp(cmd2[0], cmd2);
    perror("execvp failed");
  } else if ((pid = fork()) == 0) {
    dup2(descriptors[1], 1);
    close(descriptors[0]);

    execvp(cmd1[0], cmd1);
    perror("execvp failed");
  } else {
    waitpid(pid, NULL, 0);
  }
}

void run_redirect(char** cmd, char** filename) {
  int file = -1;
  int descriptors[2];
  pid_t pid;
  pipe(descriptors);
  
  if (fork() == 0) {
    file = open(filename[0], O_RDWR | O_CREAT, 0666);
    if (file < 0) {
      printf("Error: %s\n", strerror(errno));
      return;
    }
    if (dup2(descriptors[0], 0) < 0) {
    	printf("Error: %s\n", strerror(errno));
    	return;
    }
    close(descriptors[1]);
    
    char c;
    while (read(0, &c, 1) > 0) {
      write(file, &c, 1);
    }
    
    execlp("echo", "echo 123 123 123321", NULL);
  } else if ((pid = fork()) == 0) {
  	dup2(descriptors[1], 1);
    close(descriptors[0]);
    execvp(cmd[0], cmd);
    perror("execvp failed");
  } else {
    waitpid(pid, NULL, 0);
    close(descriptors[0]);
    close(descriptors[1]);
  }
}

CommandType parse_command(int argc, char** argv, char** cmd1, char** cmd2) {
  CommandType type = CommandType::SIMPLE;
  int split_at = -1;
  for (int i=0; i<argc; i++) {
    if (strcmp(argv[i], "|") == 0) {
      type = CommandType::PIPE;
      split_at = i;
    } else if (strcmp(argv[i], ">") == 0) {
      type = CommandType::REDIRECT;
      split_at = i;
    }
  }

  if (type != CommandType::SIMPLE) {
    for (int i=0; i < split_at; i++) {
      cmd1[i] = argv[i];
    }

    for (int i=split_at + 1; i < argc; i++) {
      cmd2[i - split_at - 1] = argv[i];
    }
    cmd1[split_at] = NULL;
    cmd2[argc - split_at] = NULL;
  }
  return type;
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