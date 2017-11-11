# lab5
own `shell`

## task
> Write a shell. It should read commands from `stdin` and start appropriate processes. Line can be split into `argv` using `strtok` or using `C++` means.

## additional tasks
1. Implement file redirection in your shell. (Use system call `dup2`)
2. Implement pipelines in your shell. (Use system call `pipe`)
3. Implement starting shell scripts (reading input commands from file) and executing commands from command line (`-c` command line argument).

## example
```sh
./myshell # usual (interactive mode)
./myshell file # script
./myshell -c "something" # command line
```

## result
> `wheel` + `shell` = `sheel` :no_bicycles: :bug: :laughing:

* **simple**:
	```sh
	Drapegnik@MacBook-Pro-Ivan:~/projects/bsu/unix-cli/lab5 (master *)$ make run
	rm -rf build
	mkdir build
	g++ -Wall sheel.cpp utils.cpp -o build/sheel
	./build/sheel
	sheel> echo lets start
	lets start
	sheel> npx cowsay -- my shell is work!
	npx: installed 9 in 2.339s
	 ___________________
	< my shell is work! >
	 -------------------
	        \   ^__^
	         \  (oo)\_______
	            (__)\       )\/\
	                ||----w |
	                ||     ||
	sheel> q
	bye!
	Drapegnik@MacBook-Pro-Ivan:~/projects/bsu/unix-cli/lab5 (master *)$
	```

* **pipe**:
	```sh
	Drapegnik@MacBook-Pro-Ivan:~/projects/bsu/unix-cli/lab5 (master *)$ make run
	rm -rf build
	mkdir build
	g++ -Wall -std=c++11 sheel.cpp utils.cpp -o build/sheel
	./build/sheel
	sheel> ls | grep .cpp
	sheel.cpp
	utils.cpp
	sheel> exit
	bye!
	Drapegnik@MacBook-Pro-Ivan:~/projects/bsu/unix-cli/lab5 (master *)$
	```

* **redirect**:
	```sh
	Drapegnik@MacBook-Pro-Ivan:~/projects/bsu/unix-cli/lab5 (master *)$ make run
	rm -rf build
	mkdir build
	g++ -Wall -std=c++11 sheel.cpp utils.cpp -o build/sheel
	./build/sheel
	sheel> echo test redirect > test.txt
	sheel> cat test.txt
	test redirect
	sheel> ^D
	Drapegnik@MacBook-Pro-Ivan:~/projects/bsu/unix-cli/lab5 (master *)$ 
	```
