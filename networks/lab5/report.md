# lab5

- _Пажитных Иван Павлович_
- _3 курс, 1 группа, МСС_
- [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab5)

# part1

## task1

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1489702414/networks-4-1.png)

- `net1`:
  - ip/mask: `176.141.64.0/26`
  - ip: `176.141.64.0`
  - mask: `255.255.255.192`
- `net2`:
  - ip/mask: `176.141.0.0/26`
  - ip: `176.141.0.0`
  - mask: `255.255.255.192`
- `net3`:
  - ip/mask: `176.141.128.0/26`
  - ip: `176.141.128.0`
  - mask: `255.255.255.192`

## task2

### Routers Serial config

- `R1` with `net2`

```
Router>enable
Router#config t
Router(config)#hostname R1
R1(config)#interface serial 0/0
R1(config-if)#ip address 176.141.0.1 255.255.255.192
R1(config-if)#clock rate 64000
R1(config-if)#no shutdown
R1(config-if)#exit
R1(config)#exit
%SYS-5-CONFIG_I: Configured from console by console
```

- `R2` with `net2`

```
Router>enable
Router#config t
Router(config)#hostname R2
R2(config)#interface serial 0/0
R2(config-if)#ip address 176.141.0.2 255.255.255.192
R2(config-if)#no shutdown
R2(config-if)#exit
R2(config)#exit
%SYS-5-CONFIG_I: Configured from console by console
```

- check connection `R1` -> `R2`:

```
R1#ping 176.141.0.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 176.141.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 15/28/46 ms
```

- check connection `R2` -> `R1`:

```
R2#ping 176.141.0.1

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 176.141.0.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 31/31/32 ms
```

### Routers FastEthernet config

- `R1` with `net1`

```
R1(config)#interface FastEthernet 0/0
R1(config-if)#ip address 176.141.64.2 255.255.255.192
R1(config-if)#no shutdown
R1(config-if)#exit
R1(config)#do copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

- `R2` with `net3`

```
R2(config)#interface FastEthernet 0/0
R2(config-if)#ip address 176.141.128.2 255.255.255.192
R2(config-if)#no shutdown
R2(config-if)#exit
R2(config)#do copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

- check connection `PC1` -> `R1`:

```
PC>ipconfig
IP Address......................: 176.141.64.1
Subnet Mask.....................: 255.255.255.192
Default Gateway.................: 176.141.64.2

PC>ping 176.141.64.2
Pinging 176.141.64.2 with 32 bytes of data:
Reply from 176.141.64.2: bytes=32 time=63ms TTL=255
Reply from 176.141.64.2: bytes=32 time=31ms TTL=255
Reply from 176.141.64.2: bytes=32 time=31ms TTL=255
Reply from 176.141.64.2: bytes=32 time=31ms TTL=255

Ping statistics for 176.141.64.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 31ms, Maximum = 63ms, Average = 39ms
```

- check connection `PC2` -> `R2`:

```
PC>ipconfig
IP Address......................: 176.141.128.1
Subnet Mask.....................: 255.255.255.192
Default Gateway.................: 176.141.128.2

PC>ping 176.141.128.2
Pinging 176.141.128.2 with 32 bytes of data:
Reply from 176.141.128.2: bytes=32 time=62ms TTL=255
Reply from 176.141.128.2: bytes=32 time=31ms TTL=255
Reply from 176.141.128.2: bytes=32 time=32ms TTL=255
Reply from 176.141.128.2: bytes=32 time=31ms TTL=255

Ping statistics for 176.141.128.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 31ms, Maximum = 62ms, Average = 39ms
```

## task 3

- set default gateway for `R1` (`net1` & `net2`)

```
R1(config)#ip route 0.0.0.0 0.0.0.0 176.141.0.2
R1(config)#ip route 176.141.64.0 255.255.255.192 176.141.0.2
```

```
R1#show ip route
Gateway of last resort is 176.141.0.2 to network 0.0.0.0
     176.141.0.0/26 is subnetted, 2 subnets
C       176.141.0.0 is directly connected, Serial0/0
C       176.141.64.0 is directly connected, FastEthernet0/0
S*   0.0.0.0/0 [1/0] via 176.141.0.2
```

- set default gateway for `R2` (`net2` & `net3`)

```
R2(config)#ip route 0.0.0.0 0.0.0.0 176.141.0.1
R2(config)#ip route 176.141.128.0 255.255.255.192 176.141.0.1
```

```
R2#show ip route
Gateway of last resort is 176.141.0.1 to network 0.0.0.0
     176.141.0.0/26 is subnetted, 2 subnets
C       176.141.0.0 is directly connected, Serial0/0
C       176.141.128.0 is directly connected, FastEthernet0/0
S*   0.0.0.0/0 [1/0] via 176.141.0.1
```

- check connection `PC1` -> `PC2`:

```
PC>ipconfig
IP Address......................: 176.141.128.1
Subnet Mask.....................: 255.255.255.192
Default Gateway.................: 176.141.128.2

PC>ping 176.141.64.1
Pinging 176.141.64.1 with 32 bytes of data:
Reply from 176.141.64.1: bytes=32 time=94ms TTL=126
Reply from 176.141.64.1: bytes=32 time=93ms TTL=126
Reply from 176.141.64.1: bytes=32 time=94ms TTL=126
Reply from 176.141.64.1: bytes=32 time=93ms TTL=126

Ping statistics for 176.141.64.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 93ms, Maximum = 94ms, Average = 93ms
```

- check connection `PC2` -> `PC1`:

```
PC>ipconfig
IP Address......................: 176.141.64.1
Subnet Mask.....................: 255.255.255.192
Default Gateway.................: 176.141.64.2

PC>ping 176.141.128.1
Pinging 176.141.128.1 with 32 bytes of data:
Reply from 176.141.128.1: bytes=32 time=94ms TTL=126
Reply from 176.141.128.1: bytes=32 time=94ms TTL=126
Reply from 176.141.128.1: bytes=32 time=94ms TTL=126
Reply from 176.141.128.1: bytes=32 time=93ms TTL=126

Ping statistics for 176.141.128.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 93ms, Maximum = 94ms, Average = 93ms
```

# part2

## task1

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1489793123/networks-4-2.png)

- `net1` - `192.168.1.0/24`
- `net2` - `192.168.2.0/24`
- `net3` - `192.168.3.0/24`
- `net4` - `192.168.4.0/24`
- `net5` - `192.168.5.0/24`
- `net6` - `192.168.6.0/24`
- `net7` - `192.168.7.0/24`

## task2

- `PC1` config

```
   Link-local IPv6 Address.........: FE80::20D:BDFF:FE14:59EC
   IP Address......................: 192.168.1.10
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 192.168.1.1
```

- `PC3` config

```
   Link-local IPv6 Address.........: FE80::260:47FF:FE6A:C31C
   IP Address......................: 192.168.4.10
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 192.168.4.1
```

- `PC4` config

```
   Link-local IPv6 Address.........: FE80::260:47FF:FE4E:857A
   IP Address......................: 192.168.6.10
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 192.168.6.1
```

- `R1` FastEthernet config

```
R1(config)#interface FastEthernet 0/0
R1(config-if)#ip address 192.168.1.1 255.255.255.0
R1(config-if)#no shutdown
```

```
R1(config)#interface FastEthernet 0/1
R1(config-if)#ip address 192.168.2.1 255.255.255.0
R1(config-if)#no shutdown
```

- `R2` FastEthernet & Serial config

```
R2(config)#interface FastEthernet 0/0
R2(config-if)#ip address 192.168.2.2 255.255.255.0
R2(config-if)#no shutdown
```

```
R2(config)#interface serial 0/0
R2(config-if)#ip address 192.168.7.1 255.255.255.0
R2(config-if)#no shutdown
```

```
R2(config)#interface serial 0/1
R2(config-if)#ip address 192.168.3.1 255.255.255.0
R2(config-if)#no shutdown
```

- `R3` FastEthernet & Serial config

```
R3(config)#interface FastEthernet 0/0
R3(config-if)#ip address 192.168.4.1 255.255.255.0
R3(config-if)#no shutdown
```

```
R3(config)#interface serial 0/0
R3(config-if)#ip address 192.168.5.1 255.255.255.0
R3(config-if)#no shutdown
```

```
R3(config)#interface serial 0/1
R3(config-if)#ip address 192.168.3.2 255.255.255.0
R3(config-if)#no shutdown
```

- `R4` FastEthernet & Serial config

```
R4(config)#interface FastEthernet 0/0
R4(config-if)#ip address 192.168.6.1 255.255.255.0
R4(config-if)#no shutdown
```

```
R4(config)#interface serial 0/0
R4(config-if)#ip address 192.168.7.2 255.255.255.0
R4(config-if)#no shutdown
```

```
R4(config)#interface serial 0/1
R4(config-if)#ip address 192.168.5.2 255.255.255.0
R4(config-if)#no shutdown
```

## task3

- set static routes for `R1`

```
R1(config)#ip route 192.168.4.0 255.255.255.0 192.168.2.2
R1(config)#ip route 192.168.6.0 255.255.255.0 192.168.2.2
```

- set static routes for `R2`

```
R2(config)#ip route 192.168.1.0 255.255.255.0 192.168.2.1
R2(config)#ip route 192.168.4.0 255.255.255.0 192.168.3.2
R2(config)#ip route 192.168.6.0 255.255.255.0 192.168.7.2
```

- set static routes for `R3`

```
R3(config)#ip route 192.168.1.0 255.255.255.0 192.168.3.1
R3(config)#ip route 192.168.6.0 255.255.255.0 192.168.5.2
```

- set static routes for `R4`

```
R4(config)#ip route 192.168.1.0 255.255.255.0 192.168.7.1
R4(config)#ip route 192.168.4.0 255.255.255.0 192.168.5.1
```

## task4

- `show ip route` for `R1`

```
    C    192.168.1.0/24 is directly connected, FastEthernet0/0
    C    192.168.2.0/24 is directly connected, FastEthernet0/1
    S    192.168.4.0/24 [1/0] via 192.168.2.2
    S    192.168.6.0/24 [1/0] via 192.168.2.2
    S*   0.0.0.0/0 [1/0] via 192.168.2.2
```

- `show ip route` for `R2`

```
    S    192.168.1.0/24 [1/0] via 192.168.2.1
    C    192.168.2.0/24 is directly connected, FastEthernet0/0
    C    192.168.3.0/24 is directly connected, Serial0/0/1
    S    192.168.4.0/24 [1/0] via 192.168.3.2
    S    192.168.6.0/24 [1/0] via 192.168.7.2
    C    192.168.7.0/24 is directly connected, Serial0/0/0
```

- `show ip route` for `R3`

```
    S    192.168.1.0/24 [1/0] via 192.168.3.1
    C    192.168.3.0/24 is directly connected, Serial0/0/1
    C    192.168.4.0/24 is directly connected, FastEthernet0/0
    C    192.168.5.0/24 is directly connected, Serial0/0/0
    S    192.168.6.0/24 [1/0] via 192.168.5.2
```

- `show ip route` for `R4`

```
    S    192.168.1.0/24 [1/0] via 192.168.7.1
    S    192.168.4.0/24 [1/0] via 192.168.5.1
    C    192.168.5.0/24 is directly connected, Serial0/0/0
    C    192.168.6.0/24 is directly connected, FastEthernet0/0
    C    192.168.7.0/24 is directly connected, Serial0/0/1
```

## task5

### `PC1` -> `PC3`

- `ping 192.168.4.10`

```
Pinging 192.168.4.10 with 32 bytes of data:
Reply from 192.168.4.10: bytes=32 time=1ms TTL=125
Reply from 192.168.4.10: bytes=32 time=1ms TTL=125
Reply from 192.168.4.10: bytes=32 time=1ms TTL=125
Reply from 192.168.4.10: bytes=32 time=1ms TTL=125
Ping statistics for 192.168.4.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms
```

- `tracert 192.168.4.10`

```
Tracing route to 192.168.4.10 over a maximum of 30 hops:
  1   0 ms      0 ms      0 ms      192.168.1.1
  2   0 ms      0 ms      0 ms      192.168.2.2
  3   0 ms      1 ms      0 ms      192.168.3.2
  4   0 ms      0 ms      0 ms      192.168.4.10
Trace complete.
```

### `PC1` -> `PC4`

- `ping 192.168.6.10`

```
Pinging 192.168.6.10 with 32 bytes of data:
Reply from 192.168.6.10: bytes=32 time=1ms TTL=125
Reply from 192.168.6.10: bytes=32 time=1ms TTL=125
Reply from 192.168.6.10: bytes=32 time=1ms TTL=125
Reply from 192.168.6.10: bytes=32 time=2ms TTL=125
Ping statistics for 192.168.6.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 2ms, Average = 1ms
```

- `tracert 192.168.6.10`

```
Tracing route to 192.168.6.10 over a maximum of 30 hops:
  1   0 ms      0 ms      0 ms      192.168.1.1
  2   0 ms      0 ms      0 ms      192.168.2.2
  3   0 ms      0 ms      1 ms      192.168.7.2
  4   1 ms      0 ms      0 ms      192.168.6.10
Trace complete.
```

### `PC3` -> `PC1`

- `ping 192.168.1.10`

```
Pinging 192.168.1.10 with 32 bytes of data:
Reply from 192.168.1.10: bytes=32 time=1ms TTL=125
Reply from 192.168.1.10: bytes=32 time=3ms TTL=125
Reply from 192.168.1.10: bytes=32 time=8ms TTL=125
Reply from 192.168.1.10: bytes=32 time=3ms TTL=125
Ping statistics for 192.168.1.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 8ms, Average = 3ms
```

- `tracert 192.168.1.10`

```
Tracing route to 192.168.1.10 over a maximum of 30 hops:
  1   0 ms      0 ms      0 ms      192.168.4.1
  2   0 ms      0 ms      1 ms      192.168.3.1
  3   0 ms      1 ms      1 ms      192.168.2.1
  4   0 ms      1 ms      14 ms     192.168.1.10
Trace complete.
```

### `PC3` -> `PC4`

- `ping 192.168.6.10`

```
Pinging 192.168.6.10 with 32 bytes of data:
Reply from 192.168.6.10: bytes=32 time=6ms TTL=126
Reply from 192.168.6.10: bytes=32 time=1ms TTL=126
Reply from 192.168.6.10: bytes=32 time=4ms TTL=126
Reply from 192.168.6.10: bytes=32 time=1ms TTL=126
Ping statistics for 192.168.6.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 6ms, Average = 3ms
```

- `tracert 192.168.6.10`

```
Tracing route to 192.168.6.10 over a maximum of 30 hops:
  1   0 ms      0 ms      0 ms      192.168.4.1
  2   1 ms      2 ms      1 ms      192.168.5.2
  3   1 ms      0 ms      1 ms      192.168.6.10
Trace complete.
```

### `PC4` -> `PC1`

- `ping 192.168.1.10`

```
Pinging 192.168.1.10 with 32 bytes of data:
Reply from 192.168.1.10: bytes=32 time=1ms TTL=125
Reply from 192.168.1.10: bytes=32 time=1ms TTL=125
Reply from 192.168.1.10: bytes=32 time=6ms TTL=125
Reply from 192.168.1.10: bytes=32 time=1ms TTL=125
Ping statistics for 192.168.1.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 6ms, Average = 2ms
```

- `tracert 192.168.1.10`

```
Tracing route to 192.168.1.10 over a maximum of 30 hops:
  1   0 ms      0 ms      0 ms      192.168.6.1
  2   0 ms      1 ms      1 ms      192.168.7.1
  3   0 ms      0 ms      0 ms      192.168.2.1
  4   0 ms      1 ms      0 ms      192.168.1.10
Trace complete.
```

### `PC4` -> `PC3`

- `ping 192.168.4.10`

```
Pinging 192.168.4.10 with 32 bytes of data:
Reply from 192.168.4.10: bytes=32 time=2ms TTL=126
Reply from 192.168.4.10: bytes=32 time=2ms TTL=126
Reply from 192.168.4.10: bytes=32 time=1ms TTL=126
Reply from 192.168.4.10: bytes=32 time=1ms TTL=126
Ping statistics for 192.168.4.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 2ms, Average = 1ms
```

- `tracert 192.168.4.10`

```
Tracing route to 192.168.4.10 over a maximum of 30 hops:
  1   0 ms      0 ms      1 ms      192.168.6.1
  2   1 ms      0 ms      0 ms      192.168.5.1
  3   0 ms      0 ms      1 ms      192.168.4.10
Trace complete.
```
