#include "sheel.h"

char *argv[MAX_ARGS];
int argc;

int main() {
	while (true) {
		cout << "sheel> ";
		argc = read_args(argv);
		if (!argc) {
			continue;
		}
		run_command(argc, argv);
	}
	return 0;
}