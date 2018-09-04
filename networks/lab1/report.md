# lab1

- _Пажитных Иван Павлович_
- _3 курс, 1 группа, МСС_
- _вариант #19_
- [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab1)

## 1. `hostname`

`MacBook-Pro-Ivan.local`

## 2. `ipconfig`

- ip-addres: `10.160.56.63`
- subnet mask: `255.255.128.0`
- gateway: `open.wifi.bsu`
- dhcp address: `10.0.0.20`
- mac-address: `72:00:06:67:22:40`
- dns-address: `10.0.0.20`

## 3. `ping`

| address     | ttl | time |
| ----------- | --- | ---- |
| 10.150.1.5  | 254 | 13ms |
| 10.150.1.1  | 126 | 28ms |
| 10.0.0.20   | 127 | 9ms  |
| 10.150.6.29 | 126 | 2ms  |
| 10.150.3.30 | 126 | 2ms  |

- `ping 10.150.1.5`:

```
PING 10.150.1.5 (10.150.1.5): 56 data bytes
64 bytes from 10.150.1.5: icmp_seq=0 ttl=254 time=12.983 ms
64 bytes from 10.150.1.5: icmp_seq=1 ttl=254 time=7.325 ms
64 bytes from 10.150.1.5: icmp_seq=2 ttl=254 time=11.669 ms
64 bytes from 10.150.1.5: icmp_seq=3 ttl=254 time=13.142 ms
64 bytes from 10.150.1.5: icmp_seq=4 ttl=254 time=101.383 ms

--- 10.150.1.5 ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 7.325/29.300/101.383/36.103 ms
```

- `ping 10.150.1.1`:

```
PING 10.150.1.1 (10.150.1.1): 56 data bytes
64 bytes from 10.150.1.1: icmp_seq=0 ttl=126 time=40.251 ms
64 bytes from 10.150.1.1: icmp_seq=1 ttl=126 time=9.657 ms
64 bytes from 10.150.1.1: icmp_seq=2 ttl=126 time=3.135 ms
64 bytes from 10.150.1.1: icmp_seq=3 ttl=126 time=28.235 ms
64 bytes from 10.150.1.1: icmp_seq=4 ttl=126 time=5.278 ms

--- 10.150.1.1 ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.135/17.311/40.251/14.491 ms
```

- `ping 10.0.0.20`:

```
PING 10.0.0.20 (10.0.0.20): 56 data bytes
64 bytes from 10.0.0.20: icmp_seq=0 ttl=127 time=3.809 ms
64 bytes from 10.0.0.20: icmp_seq=1 ttl=127 time=3.546 ms
64 bytes from 10.0.0.20: icmp_seq=2 ttl=127 time=9.281 ms
64 bytes from 10.0.0.20: icmp_seq=3 ttl=127 time=17.810 ms
64 bytes from 10.0.0.20: icmp_seq=4 ttl=127 time=12.888 ms

--- 10.0.0.20 ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.546/9.467/17.810/5.448 ms
```

- `ping 10.150.6.29`:

```
PING 10.150.6.29 (10.150.6.29): 56 data bytes
64 bytes from 10.150.6.29: icmp_seq=0 ttl=126 time=5.058 ms
64 bytes from 10.150.6.29: icmp_seq=1 ttl=126 time=4.163 ms
64 bytes from 10.150.6.29: icmp_seq=2 ttl=126 time=1.922 ms
64 bytes from 10.150.6.29: icmp_seq=3 ttl=126 time=1.946 ms
64 bytes from 10.150.6.29: icmp_seq=4 ttl=126 time=1.847 ms

--- 10.150.6.29 ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 1.847/2.987/5.058/1.356 ms
```

- `ping 10.150.3.30`:

```
PING 10.150.3.30 (10.150.3.30): 56 data bytes
64 bytes from 10.150.3.30: icmp_seq=0 ttl=126 time=1.469 ms
64 bytes from 10.150.3.30: icmp_seq=1 ttl=126 time=28.628 ms
64 bytes from 10.150.3.30: icmp_seq=2 ttl=126 time=2.202 ms
64 bytes from 10.150.3.30: icmp_seq=3 ttl=126 time=2.161 ms
64 bytes from 10.150.3.30: icmp_seq=4 ttl=126 time=2.090 ms

--- 10.150.3.30 ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 1.469/7.310/28.628/10.662 ms
```

| address    | ip             | time |
| ---------- | -------------- | ---- |
| ya.ru      | 93.158.134.3   | 78ms |
| yandex.ru  | 5.255.255.55   | 64ms |
| tut.by     | 178.172.160.2  | 7ms  |
| onliner.by | 178.124.129.14 | 9ms  |

- `ping ya.ru`:

```
PING ya.ru (93.158.134.3): 56 data bytes
64 bytes from 93.158.134.3: icmp_seq=0 ttl=51 time=78.590 ms
64 bytes from 93.158.134.3: icmp_seq=1 ttl=51 time=78.794 ms
64 bytes from 93.158.134.3: icmp_seq=2 ttl=51 time=79.144 ms
64 bytes from 93.158.134.3: icmp_seq=3 ttl=51 time=79.358 ms
64 bytes from 93.158.134.3: icmp_seq=4 ttl=51 time=78.066 ms

--- ya.ru ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 78.066/78.790/79.358/0.450 ms
```

- `ping yandex.ru`:

```
PING yandex.ru (5.255.255.55): 56 data bytes
64 bytes from 5.255.255.55: icmp_seq=0 ttl=52 time=62.885 ms
64 bytes from 5.255.255.55: icmp_seq=1 ttl=52 time=66.083 ms
64 bytes from 5.255.255.55: icmp_seq=2 ttl=52 time=64.771 ms
64 bytes from 5.255.255.55: icmp_seq=3 ttl=52 time=64.913 ms
64 bytes from 5.255.255.55: icmp_seq=4 ttl=52 time=67.250 ms

--- yandex.ru ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 62.885/65.180/67.250/1.456 ms
```

- `ping tut.by`:

```
PING tut.by (178.172.160.2): 56 data bytes
64 bytes from 178.172.160.2: icmp_seq=0 ttl=57 time=3.890 ms
64 bytes from 178.172.160.2: icmp_seq=1 ttl=57 time=6.985 ms
64 bytes from 178.172.160.2: icmp_seq=2 ttl=57 time=5.929 ms
64 bytes from 178.172.160.2: icmp_seq=3 ttl=57 time=18.421 ms
64 bytes from 178.172.160.2: icmp_seq=4 ttl=57 time=3.704 ms

--- tut.by ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.704/7.786/18.421/5.460 ms
```

- `ping -c 19 -s 1000 onliner.by`:

```
PING onliner.by (178.124.129.14): 1000 data bytes
1008 bytes from 178.124.129.14: icmp_seq=0 ttl=57 time=3.881 ms
1008 bytes from 178.124.129.14: icmp_seq=1 ttl=57 time=27.734 ms
1008 bytes from 178.124.129.14: icmp_seq=2 ttl=57 time=4.349 ms
1008 bytes from 178.124.129.14: icmp_seq=3 ttl=57 time=6.633 ms
1008 bytes from 178.124.129.14: icmp_seq=4 ttl=57 time=15.975 ms
1008 bytes from 178.124.129.14: icmp_seq=5 ttl=57 time=7.877 ms
1008 bytes from 178.124.129.14: icmp_seq=6 ttl=57 time=3.745 ms
1008 bytes from 178.124.129.14: icmp_seq=7 ttl=57 time=8.865 ms
1008 bytes from 178.124.129.14: icmp_seq=8 ttl=57 time=10.251 ms
1008 bytes from 178.124.129.14: icmp_seq=9 ttl=57 time=4.258 ms
1008 bytes from 178.124.129.14: icmp_seq=10 ttl=57 time=3.463 ms
1008 bytes from 178.124.129.14: icmp_seq=11 ttl=57 time=3.971 ms
1008 bytes from 178.124.129.14: icmp_seq=12 ttl=57 time=3.804 ms
1008 bytes from 178.124.129.14: icmp_seq=13 ttl=57 time=3.085 ms
1008 bytes from 178.124.129.14: icmp_seq=14 ttl=57 time=11.908 ms
1008 bytes from 178.124.129.14: icmp_seq=15 ttl=57 time=3.868 ms
1008 bytes from 178.124.129.14: icmp_seq=16 ttl=57 time=4.033 ms
1008 bytes from 178.124.129.14: icmp_seq=17 ttl=57 time=4.006 ms
1008 bytes from 178.124.129.14: icmp_seq=18 ttl=57 time=5.871 ms

--- onliner.by ping statistics ---
19 packets transmitted, 19 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.085/7.241/27.734/5.891 ms
```

- `ping localhost`:

```
PING localhost (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.042 ms
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.152 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.144 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.128 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.121 ms

--- localhost ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.042/0.117/0.152/0.039 ms
```

## 4. `traceroute`

- `traceroute -d tut.by:`

```
 1  open.wifi.bsu (10.160.0.1)  2.691 ms  1.205 ms  1.151 ms
 2  border-gw.net.bsu (10.149.8.252)  1.170 ms  3.122 ms  1.241 ms
 3  * * *
 4  * * *
 5  * 195.137.180.124 (195.137.180.124)  22.113 ms  2.973 ms
 6  * 93.84.125.193 (93.84.125.193)  17.016 ms  10.495 ms
 7  * 178.124.134.214 (178.124.134.214)  34.262 ms  2.414 ms
 8  * * *
 9  178-172-160-2.hosterby.com (178.172.160.2)  2.664 ms  2.034 ms  1.870 ms
```

- `traceroute -m 8 onliner.by`

```
 1  open.wifi.bsu (10.160.0.1)  3.157 ms  3.358 ms  3.689 ms
 2  border-gw.net.bsu (10.149.8.252)  2.687 ms  3.225 ms  3.351 ms
 3  * * *
 4  * * *
 5  195.137.180.124 (195.137.180.124)  7.355 ms  11.189 ms  6.307 ms
 6  * 93.84.125.189 (93.84.125.189)  12.684 ms  12.394 ms
 7  178.124.134.214 (178.124.134.214)  2.132 ms  3.416 ms  2.957 ms
 8  * onliner.by (178.124.129.14)  5.241 ms  3.162 ms
```

## 5. `arp`

- `arp -a`

```
open.wifi.bsu (10.160.0.1) at 0:21:a0:c1:19:40 on en0 ifscope [ethernet]
? (10.160.127.255) at (incomplete) on en0 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
```

## 6. `netstat`

- `netstat -p TCP`

```
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  10.160.56.63.54536     23.99.116.116.https    ESTABLISHED
tcp4       0      0  10.160.56.63.54535     23.99.116.116.https    ESTABLISHED
tcp4       0      0  10.160.56.63.54534     23.99.116.116.https    ESTABLISHED
tcp4       0      0  10.160.56.63.54530     janus2.intuit.ru.http  ESTABLISHED
tcp4       0      0  10.160.56.63.54525     17.110.232.46.https    ESTABLISHED
tcp4       0      0  10.160.56.63.54523     17.154.66.159.http     ESTABLISHED
tcp4       0      0  10.160.56.63.54519     ec2-52-203-218-1.https ESTABLISHED
tcp4       0      0  10.160.56.63.54518     waw02s06-in-f10..https ESTABLISHED
tcp4       0      0  10.160.56.63.54517     waw02s06-in-f78..https ESTABLISHED
tcp4       0      0  10.160.56.63.54512     waw02s07-in-f3.1.https ESTABLISHED
tcp4       0      0  10.160.56.63.54511     95.213.11.180.https    ESTABLISHED
tcp4       0      0  10.160.56.63.54508     srv82-165-240-87.https ESTABLISHED
tcp4       0      0  10.160.56.63.54500     149.154.167.51.https   ESTABLISHED
tcp4       0      0  10.160.56.63.54498     95.213.4.194.https     ESTABLISHED
tcp4       0      0  10.160.56.63.54497     ec2-52-0-252-241.https ESTABLISHED
tcp4       0      0  10.160.56.63.54487     waw02s06-in-f5.1.https ESTABLISHED
tcp4       0      0  10.160.56.63.54486     waw02s06-in-f78..https ESTABLISHED
tcp4       0      0  10.160.56.63.54485     waw02s06-in-f78..https ESTABLISHED
tcp4       0      0  10.160.56.63.54477     waw02s06-in-f78..https ESTABLISHED
tcp4       0      0  10.160.56.63.54474     li-in-f188.1e100.https ESTABLISHED
tcp4       0      0  10.160.56.63.54471     17.188.165.204.5223    ESTABLISHED
tcp4       0      0  10.160.56.63.54469     17.188.139.40.5223     ESTABLISHED
tcp4       0      0  10.160.56.63.54466     lt-in-f189.1e100.https ESTABLISHED
tcp4       0      0  10.160.56.63.54464     157.55.235.154.40023   ESTABLISHED
tcp4       0      0  10.160.56.63.54463     waw02s06-in-f4.1.https ESTABLISHED
tcp4       0      0  10.160.56.63.54462     137.116.172.9.https    ESTABLISHED
tcp4       0      0  10.160.56.63.54460     91.190.217.44.12350    ESTABLISHED
tcp4       0      0  10.160.56.63.54459     40.77.226.192.https    ESTABLISHED
tcp4       0      0  cmm-server.54422       192.30.253.124.https   ESTABLISHED
tcp4       0      0  cmm-server.54044       192.30.253.125.https   ESTABLISHED
tcp4       0      0  10.160.56.63.54521     23.97.178.173.https    TIME_WAIT
tcp4       0      0  10.160.56.63.54524     23.97.178.173.https    TIME_WAIT
tcp4       0      0  10.160.56.63.54527     janus2.intuit.ru.http  TIME_WAIT
tcp4       0      0  10.160.56.63.54528     janus2.intuit.ru.http  TIME_WAIT
tcp4       0      0  10.160.56.63.54529     janus2.intuit.ru.http  TIME_WAIT
tcp4       0      0  10.160.56.63.54531     janus2.intuit.ru.http  TIME_WAIT
tcp4       0      0  10.160.56.63.54532     janus2.intuit.ru.http  TIME_WAIT
tcp4       0      0  10.160.56.63.54533     janus2.intuit.ru.http  TIME_WAIT
tcp4       0      0  10.160.56.63.54526     104.40.208.40.https    TIME_WAIT
```

- `netstat -np TCP`

```
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  10.160.56.63.55750     52.72.183.95.443       ESTABLISHED
tcp4       0      0  10.160.56.63.55748     216.58.209.46.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55746     216.58.209.46.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55744     216.58.209.78.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55740     216.58.209.78.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55739     216.58.209.67.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55729     192.30.253.125.443     ESTABLISHED
tcp4       0      0  10.160.56.63.55718     151.101.36.133.443     ESTABLISHED
tcp4       0      0  10.160.56.63.55716     17.188.165.202.5223    ESTABLISHED
tcp4       0      0  10.160.56.63.55699     52.0.252.241.443       ESTABLISHED
tcp4       0      0  10.160.56.63.55606     95.213.4.194.443       ESTABLISHED
tcp4       0      0  10.160.56.63.55603     87.240.165.82.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55579     64.233.165.188.443     ESTABLISHED
tcp4       0      0  10.160.56.63.55575     17.188.147.48.5223     ESTABLISHED
tcp4       0      0  10.160.56.63.55573     209.85.233.189.443     ESTABLISHED
tcp4       0      0  10.160.56.63.55571     111.221.77.143.40004   ESTABLISHED
tcp4       0      0  10.160.56.63.55541     149.154.167.51.443     ESTABLISHED
tcp4       0      0  10.160.56.63.55531     207.46.151.217.443     ESTABLISHED
tcp4       0      0  10.160.56.63.55530     40.77.226.192.443      ESTABLISHED
tcp4       0      0  10.160.56.63.55529     91.190.216.53.12350    ESTABLISHED
tcp4       0      0  10.160.56.63.54662     192.30.253.125.443     ESTABLISHED
```

- `netstat –a –s –r`

`netstat -r` - Show the routing tables. Use with `-a` to show protocol-cloned
routes. When `-s` is also present, show routing statistics instead

```
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  10.160.56.63.55750     ec2-52-72-183-95.https ESTABLISHED
tcp4       0      0  10.160.56.63.55748     waw02s05-in-f14..https ESTABLISHED
tcp4       0      0  10.160.56.63.55746     waw02s05-in-f14..https ESTABLISHED
tcp4       0      0  10.160.56.63.55744     waw02s06-in-f14..https ESTABLISHED
tcp4       0      0  10.160.56.63.55740     waw02s06-in-f14..https ESTABLISHED
tcp4       0      0  10.160.56.63.55739     waw02s06-in-f3.1.https ESTABLISHED
tcp4       0      0  10.160.56.63.55729     192.30.253.125.https   ESTABLISHED
tcp4       0      0  10.160.56.63.55718     151.101.36.133.https   ESTABLISHED
tcp4       0      0  10.160.56.63.55716     17.188.165.202.5223    ESTABLISHED
tcp4       0      0  10.160.56.63.55699     ec2-52-0-252-241.https ESTABLISHED
tcp4       0      0  10.160.56.63.55606     95.213.4.194.https     ESTABLISHED
tcp4       0      0  10.160.56.63.55603     srv82-165-240-87.https ESTABLISHED
tcp4       0      0  10.160.56.63.55579     lg-in-f188.1e100.https ESTABLISHED
tcp4       0      0  10.160.56.63.55575     17.188.147.48.5223     ESTABLISHED
tcp4       0      0  10.160.56.63.55573     lr-in-f189.1e100.https ESTABLISHED
tcp4       0      0  10.160.56.63.55571     111.221.77.143.40004   ESTABLISHED
tcp4       0      0  10.160.56.63.55541     149.154.167.51.https   ESTABLISHED
tcp4       0      0  10.160.56.63.55531     207.46.151.217.https   ESTABLISHED
tcp4       0      0  10.160.56.63.55530     40.77.226.192.https    ESTABLISHED
tcp4       0      0  10.160.56.63.55529     91.190.216.53.12350    ESTABLISHED
tcp4       0      0  10.160.56.63.54662     192.30.253.125.https   ESTABLISHED
udp4       0      0  10.160.56.63.59972     waw02s05-in-f14..https
udp4       0      0  10.160.56.63.58351     lt-in-f189.1e100.https
udp6       0      0  *.65482                *.*
udp4       0      0  *.65482                *.*
udp6       0      0  *.55840                *.*
udp4       0      0  *.55840                *.*
udp6       0      0  *.49809                *.*
udp4       0      0  *.49809                *.*
udp6       0      0  *.50470                *.*
udp4       0      0  *.50470                *.*
udp4       0      0  10.160.56.63.21767     *.*
udp4       0      0  *.*                    *.*
udp4       0      0  10.160.56.63.ntp       *.*
udp6       0      0  fe80::47f:d7bc:8.ntp   *.*
udp6       0      0  fe80::4479:65ff:.ntp   *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp46      0      0  *.53117                *.*
udp4       0      0  *.*                    *.*
udp4       0      0  localhost.53116        *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.58403                *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp6       0      0  fe80::e41a:ed2d:.ntp   *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp6       0      0  fe80::1%lo0.ntp        *.*
udp6       0      0  localhost.ntp          *.*
udp4       0      0  localhost.ntp          *.*
udp4       0      0  *.ntp                  *.*
udp6       0      0  *.ntp                  *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp46      0      0  *.*                    *.*
udp6       0      0  *.mdns                 *.*
udp4       0      0  *.mdns                 *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.*                    *.*
udp4       0      0  *.netbios-ns           *.*
udp4       0      0  *.netbios-dgm          *.*
Active Multipath Internet connections
Proto/ID  Flags      Local Address          Foreign Address        (state)
icm6       0      0  *.*                    *.*
Active LOCAL (UNIX) domain sockets
Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
f744bf24a76c949f stream      0      0                0 f744bf24a76cbe07                0                0
f744bf24a76c962f stream      0      0                0 f744bf24a76c97bf                0                0
f744bf24a76c97bf stream      0      0                0 f744bf24a76c962f                0                0
f744bf24a76c930f stream      0      0                0 f744bf24a76c9adf                0                0
f744bf24a76c9adf stream      0      0                0 f744bf24a76c930f                0                0
f744bf249c135a17 stream      0      0                0 f744bf249c135dff                0                0
f744bf24acb764a7 stream      0      0                0 f744bf24acb74d37                0                0
f744bf24acb74d37 stream      0      0                0 f744bf24acb764a7                0                0
f744bf24acb759b7 stream      0      0                0 f744bf24acb75cd7                0                0
f744bf24acb75cd7 stream      0      0                0 f744bf24acb759b7                0                0
f744bf24acb7575f stream      0      0                0 f744bf24acb74adf                0                0
f744bf24acb74adf stream      0      0                0 f744bf24acb7575f                0                0
f744bf24acb763df stream      0      0                0 f744bf24acb760bf                0                0
f744bf24a76cad9f stream      0      0                0 f744bf24a76cb6ff                0                0
f744bf24a76cb4a7 stream      0      0                0 f744bf24a76cbae7                0                0
f744bf24a76cbae7 stream      0      0                0 f744bf24a76cb4a7                0                0
f744bf24a76c9247 stream      0      0                0                0                0                0
f744bf249ec92c77 stream      0      0                0 f744bf249ec923df                0                0
f744bf249ec923df stream      0      0                0 f744bf249ec92c77                0                0
f744bf249ec92ae7 stream      0      0                0 f744bf24b75955cf                0                0
f744bf24acb76c77 stream      0      0                0 f744bf24acb7494f                0                0
f744bf24acb74887 stream      0      0                0 f744bf24acb75827                0                0
f744bf24acb75827 stream      0      0                0 f744bf24acb74887                0                0
f744bf24acb766ff stream      0      0                0 f744bf24acb740b7                0                0
f744bf24acb740b7 stream      0      0                0 f744bf24acb766ff                0                0
f744bf24acb75d9f stream      0      0                0 f744bf24acb7656f                0                0
f744bf24acb7656f stream      4      0                0 f744bf24acb75d9f                0                0
f744bf24acb747bf stream      0      0                0 f744bf24acb74567                0                0
f744bf24acb74567 stream      0      0                0 f744bf24acb747bf                0                0
f744bf24acb751e7 stream      0      0                0 f744bf24acb73fef                0                0
f744bf249c13530f stream      0      0                0 f744bf249c134f27                0                0
f744bf249c137187 stream      0      0                0 f744bf249c13788f                0                0
f744bf249c13788f stream      0      0                0 f744bf249c137187                0                0
f744bf249c1376ff stream      0      0                0 f744bf249c136507                0                0
f744bf249c136507 stream      0      0                0 f744bf249c1376ff                0                0
f744bf249c137637 stream      0      0                0 f744bf249c1370bf                0                0
f744bf249c1370bf stream      0      0                0 f744bf249c137637                0                0
f744bf249c1350b7 stream      0      0                0 f744bf249c13756f                0                0
f744bf249c13756f stream      0      0                0 f744bf249c1350b7                0                0
f744bf249c1361e7 stream      0      0                0 f744bf249c135567                0                0
f744bf249c135567 stream      0      0                0 f744bf249c1361e7                0                0
f744bf249ec926ff stream      0      0                0 f744bf249ec90a17                0                0
f744bf249ec90a17 stream      0      0                0 f744bf249ec926ff                0                0
Registered kernel control modules
id       flags    pcbcount rcvbuf   sndbuf   name
       1        9        0   131072   131072 com.apple.flow-divert
       2        1        0    16384     2048 com.apple.nke.sockwall
       3        9        0   524288   524288 com.apple.content-filter
       4        9        0     8192     2048 com.apple.packet-mangler
       5        1        3    65536    65536 com.apple.net.necp_control
       6        1       10    65536    65536 com.apple.net.netagent
       7        9        1   524288   524288 com.apple.net.utun_control
       8        1        0    65536    65536 com.apple.net.ipsec_control
       9        0       21     8192     2048 com.apple.netsrc
       a       18        5     8192     2048 com.apple.network.statistics
       b        5        0     8192     2048 com.apple.network.tcp_ccdebug
       c        1        1     8192     2048 com.apple.network.advisory
       d        1        1     8192     2048 com.checkpoint.cpfw.ctl
       e        1        0     8192     2048 com.checkpoint.cpfw.fwnotify
       f        1        0  1048576     2048 com.checkpoint.cpfw.debug
Active kernel event sockets
Proto Recv-Q Send-Q vendor  class subcla
kevt       0      0      1      1     11
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      1      7
kevt       0      0      1      1      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      1      0
Active kernel control sockets
Proto Recv-Q Send-Q   unit     id name
kctl       0      0      1      5 com.apple.net.necp_control
kctl       0      0      2      5 com.apple.net.necp_control
kctl       0      0      3      5 com.apple.net.necp_control
kctl       0      0      1      6 com.apple.net.netagent
kctl       0      0      2      6 com.apple.net.netagent
kctl       0      0      3      6 com.apple.net.netagent
kctl       0      0      4      6 com.apple.net.netagent
kctl       0      0      5      6 com.apple.net.netagent
kctl       0      0      6      6 com.apple.net.netagent
kctl       0      0      7      6 com.apple.net.netagent
kctl       0      0      8      6 com.apple.net.netagent
kctl       0      0      9      6 com.apple.net.netagent
kctl       0      0     10      6 com.apple.net.netagent
kctl       0      0      1      7 com.apple.net.utun_control
kctl       0      0      1      9 com.apple.netsrc
kctl       0      0      2      9 com.apple.netsrc
kctl       0      0      3      9 com.apple.netsrc
kctl       0      0      4      9 com.apple.netsrc
kctl       0      0      5      9 com.apple.netsrc
kctl       0      0      6      9 com.apple.netsrc
kctl       0      0      7      9 com.apple.netsrc
kctl       0      0      8      9 com.apple.netsrc
kctl       0      0      9      9 com.apple.netsrc
kctl       0      0     10      9 com.apple.netsrc
kctl       0      0     11      9 com.apple.netsrc
kctl       0      0     12      9 com.apple.netsrc
kctl       0      0     13      9 com.apple.netsrc
kctl       0      0     15      9 com.apple.netsrc
kctl       0      0     16      9 com.apple.netsrc
kctl       0      0     17      9 com.apple.netsrc
kctl       0      0     18      9 com.apple.netsrc
kctl       0      0     22      9 com.apple.netsrc
kctl       0      0     24      9 com.apple.netsrc
kctl       0      0     25      9 com.apple.netsrc
kctl       0      0     26      9 com.apple.netsrc
kctl       0      0      1     10 com.apple.network.statistics
kctl       0      0      2     10 com.apple.network.statistics
kctl       0      0      3     10 com.apple.network.statistics
kctl       0      0      4     10 com.apple.network.statistics
kctl       0      0      5     10 com.apple.network.statistics
kctl       0      0      1     12 com.apple.network.advisory
kctl       0      0      1     13 com.checkpoint.cpfw.ctl
```

## 7. `nslookup`

- `nslookup 10.150.5.44`

```
Server:		10.0.0.20
Address:	10.0.0.20#53

44.5.150.10.in-addr.arpa	name = fpmi506st14.bsu.
```

## 8. `route`

- `netstat -rn`

```
Routing tables

Internet:
Destination        Gateway            Flags        Refs      Use   Netif Expire
default            10.160.0.1         UGSc          224      105     en0
10.160/17          link#4             UCS             2        0     en0
10.160.0.1/32      link#4             UCS             2        0     en0
10.160.0.1         0:21:a0:c1:19:40   UHLWIir       225       28     en0    969
10.160.56.63/32    link#4             UCS             1        0     en0
10.160.127.255     link#4             UHLWbI          1       18     en0
127                127.0.0.1          UCS             1        0     lo0
127.0.0.1          127.0.0.1          UH              3    31728     lo0
224.0.0/4          link#4             UmCS            3        0     en0
224.0.0.251        1:0:5e:0:0:fb      UHmLWI          1        0     en0
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI          1       20     en0
255.255.255.255/32 link#4             UCS             1        0     en0

Internet6:
Destination                             Gateway                         Flags         Netif Expire
default                                 fe80::%utun0                    UGcI          utun0
::1                                     ::1                             UHL             lo0
fe80::%lo0/64                           fe80::1%lo0                     UcI             lo0
fe80::1%lo0                             link#1                          UHLI            lo0
fe80::%en0/64                           link#4                          UCI             en0
fe80::47f:d7bc:8963:5392%en0            6c:40:8:a8:e3:e0                UHLI            lo0
fe80::%awdl0/64                         link#8                          UCI           awdl0
fe80::4479:65ff:feeb:a9dd%awdl0         46:79:65:eb:a9:dd               UHLI            lo0
fe80::%utun0/64                         fe80::e41a:ed2d:46c4:7416%utun0 UcI           utun0
fe80::e41a:ed2d:46c4:7416%utun0         link#10                         UHLI            lo0
ff01::%lo0/32                           ::1                             UmCI            lo0
ff01::%en0/32                           link#4                          UmCI            en0
ff01::%awdl0/32                         link#8                          UmCI          awdl0
ff01::%utun0/32                         fe80::e41a:ed2d:46c4:7416%utun0 UmCI          utun0
ff02::%lo0/32                           ::1                             UmCI            lo0
ff02::%en0/32                           link#4                          UmCI            en0
ff02::%awdl0/32                         link#8                          UmCI          awdl0
ff02::%utun0/32                         fe80::e41a:ed2d:46c4:7416%utun0 UmCI          utun0
```
