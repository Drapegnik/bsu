#include "sheel.h"

char *argv[MAX_ARGS], *cmd1[MAX_ARGS], *cmd2[MAX_ARGS];

int main() {
	while (true) {
		cout << "sheel> ";
		int argc = read_args(argv);
		if (!argc) {
			continue;
		}
		CommandType type = parse_command(argc, argv, cmd1, cmd2);
		if (type == CommandType::PIPE) {
			run_pipe(cmd1, cmd2);
		} else if (type == CommandType::REDIRECT) {
			run_redirect(cmd1, cmd2);
		} else {
			run_command(argc, argv);
		}
	}
	return 0;
}