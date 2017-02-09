# lab1
by Ivan Pazhitnykh

## 1. `hostname`
`MBP-Ivan`
## 2. `ipconfig`
 * ip-addres:		`192.168.0.187`
 * subnet mask:		`255.255.255.0`
 * gateway:		`192.168.0.1`
 * dhcp address:	`192.168.0.1`
 * mac-address:		`72:00:06:67:22:40`
 * dns-address:		`192.168.0.1`

## 3. `ping`
 * `ping  ya.ru`:
```
PING ya.ru (93.158.134.3): 56 data bytes
64 bytes from 93.158.134.3: icmp_seq=0 ttl=53 time=59.637 ms
64 bytes from 93.158.134.3: icmp_seq=1 ttl=53 time=53.473 ms
64 bytes from 93.158.134.3: icmp_seq=2 ttl=53 time=70.222 ms
64 bytes from 93.158.134.3: icmp_seq=3 ttl=53 time=48.218 ms
64 bytes from 93.158.134.3: icmp_seq=4 ttl=53 time=82.306 ms

--- ya.ru ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 48.218/62.771/82.306/12.208 ms
```
 * `ping  yandex.ru`:
```
PING yandex.ru (5.255.255.50): 56 data bytes
64 bytes from 5.255.255.50: icmp_seq=0 ttl=52 time=77.175 ms
64 bytes from 5.255.255.50: icmp_seq=1 ttl=52 time=114.173 ms
64 bytes from 5.255.255.50: icmp_seq=2 ttl=52 time=91.003 ms
64 bytes from 5.255.255.50: icmp_seq=3 ttl=52 time=48.937 ms
64 bytes from 5.255.255.50: icmp_seq=4 ttl=52 time=266.798 ms

--- yandex.ru ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 48.937/119.617/266.798/76.561 ms
```
 * `ping  tut.by`:
```
PING tut.by (178.172.160.5): 56 data bytes
64 bytes from 178.172.160.5: icmp_seq=0 ttl=55 time=27.654 ms
64 bytes from 178.172.160.5: icmp_seq=1 ttl=55 time=93.901 ms
64 bytes from 178.172.160.5: icmp_seq=2 ttl=55 time=41.506 ms
64 bytes from 178.172.160.5: icmp_seq=3 ttl=55 time=82.318 ms
64 bytes from 178.172.160.5: icmp_seq=4 ttl=55 time=62.512 ms

--- tut.by ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.654/61.578/93.901/24.615 ms
```
 * `ping -c 19 -s 1000 onliner.by`:
```
PING onliner.by (178.124.129.16): 1000 data bytes
1008 bytes from 178.124.129.16: icmp_seq=0 ttl=56 time=39.911 ms
1008 bytes from 178.124.129.16: icmp_seq=1 ttl=56 time=58.323 ms
1008 bytes from 178.124.129.16: icmp_seq=2 ttl=56 time=52.800 ms
1008 bytes from 178.124.129.16: icmp_seq=3 ttl=56 time=48.908 ms
1008 bytes from 178.124.129.16: icmp_seq=4 ttl=56 time=58.997 ms
