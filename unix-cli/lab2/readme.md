# lab2

low-level file write/open on `C++`, `dtrace` command

## result

* `bash run.sh`:

```
#compiled.
#file contains: Lol
#truss:
dtrace: system integrity protection is on, some features will not be available

SYSCALL(args) 		 = return
open("/dev/dtracehelper\0", 0x2, 0x7FFF59F5F660)		 = 3 0
ioctl(0x3, 0x80086804, 0x7FFF59F5F5E8)		 = 0 0
close(0x3)		 = 0 0
thread_selfid(0x3, 0x80086804, 0x7FFF59F5F5E8)		 = 6148480 0
bsdthread_register(0x7FFF9BDAB080, 0x7FFF9BDAB070, 0x2000)		 = 1073741919 0
ulock_wake(0x1, 0x7FFF59F5EE1C, 0x0)		 = -1 Err#2
issetugid(0x1, 0x7FFF59F5EE1C, 0x0)		 = 0 0
mprotect(0x105CA4000, 0x88, 0x1)		 = 0 0
mprotect(0x105CA6000, 0x1000, 0x0)		 = 0 0
mprotect(0x105CBC000, 0x1000, 0x0)		 = 0 0
mprotect(0x105CBD000, 0x1000, 0x0)		 = 0 0
mprotect(0x105CD3000, 0x1000, 0x0)		 = 0 0
mprotect(0x105CD4000, 0x1000, 0x1)		 = 0 0
mprotect(0x105CA4000, 0x88, 0x3)		 = 0 0
mprotect(0x105CA4000, 0x88, 0x1)		 = 0 0
getpid(0x105CA4000, 0x88, 0x1)		 = 64122 0
stat64("/AppleInternal/XBS/.isChrooted\0", 0x7FFF59F5ECD8, 0x1)		 = -1 Err#2
stat64("/AppleInternal\0", 0x7FFF59F5ED70, 0x1)		 = -1 Err#2
csops(0xFA7A, 0x7, 0x7FFF59F5E800)		 = -1 Err#22
dtrace: error on enabled probe ID 2158 (ID 561: syscall::sysctl:return): invalid kernel access in action #10 at DIF offset 40
ulock_wake(0x1, 0x7FFF59F5ED80, 0x0)		 = -1 Err#2
csops(0xFA7A, 0x7, 0x7FFF59F5E0E0)		 = -1 Err#22
open("lala.txt\0", 0x201, 0x7FFF59F60920)		 = 3 0
dtrace: error on enabled probe ID 2132 (ID 165: syscall::write:return): invalid kernel access in action #12 at DIF offset 92
```
