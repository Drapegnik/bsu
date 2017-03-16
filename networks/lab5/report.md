# lab5
* *Пажитных Иван Павлович*
* *3 курс, 1 группа, МСС*
* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab5)

# part1
## task1
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1489702414/networks-4-1.png)

* `net1`:
    * ip/mask: `176.141.64.0/26`
    * ip: `176.141.64.0`
    * mask: `255.255.255.192`
* `net2`:
    * ip/mask: `176.141.0.0/26`
    * ip: `176.141.0.0`
    * mask: `255.255.255.192`
* `net3`:
    * ip/mask: `176.141.128.0/26`
    * ip: `176.141.128.0`
    * mask: `255.255.255.192`

## task2

### Routers Serial config for `net2`

#### R1
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

#### R2
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

#### Check connection:
```
R1#ping 176.141.0.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 176.141.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 15/28/46 ms
```

```
R2#ping 176.141.0.1

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 176.141.0.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 31/31/32 ms
```

### Routers FastEthernet config

#### R1 with `net1`

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

#### R2 with `net3`

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

#### Check connection for `PC1` in `net1`
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

#### Check connection for `PC2` in `net3`

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

### Set default gateway for `R1` (`net1` & `net2`)
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

### Set default gateway for `R2` (`net2` & `net3`)
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

### Check connection between `PC1` and `PC2`

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