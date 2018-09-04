# lab9

- _Пажитных Иван Павлович_
- _3 курс, 1 группа, МСС_
- [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab9)

# part1

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491837213/networks9-1.png)

## task1 - subnets:

- `net1` ~ `50`

| name      | value               |
| --------- | ------------------- |
| ip/mask   | `176.141.64.128/26` |
| ip        | `176.141.64.128`    |
| mask      | `255.255.255.192`   |
| net size  | `62`                |
| min addr  | `176.141.64.129`    |
| max addr  | `176.141.64.190`    |
| broadcast | `176.141.64.191`    |

- `net2` ~ `2`

| name      | value               |
| --------- | ------------------- |
| ip/mask   | `176.141.64.192/30` |
| ip        | `176.141.64.192`    |
| mask      | `255.255.255.252`   |
| net size  | `2`                 |
| min addr  | `176.141.64.193`    |
| max addr  | `176.141.64.194`    |
| broadcast | `176.141.64.195`    |

- `net3` ~ `100`

| name      | value             |
| --------- | ----------------- |
| ip/mask   | `176.141.64.0/25` |
| ip        | `176.141.64.0`    |
| mask      | `255.255.255.128` |
| net size  | `126`             |
| min addr  | `176.141.64.1`    |
| max addr  | `176.141.64.126`  |
| broadcast | `176.141.64.127`  |

## task2 - ip configs

- `PC0` in `net1`

```
   Link-local IPv6 Address.........: FE80::201:97FF:FE28:C205
   IP Address......................: 176.141.64.130
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.64.129
```

- `PC1` in `net1`

```
   Link-local IPv6 Address.........: FE80::203:E4FF:FE42:1323
   IP Address......................: 176.141.64.131
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.64.129
```

- `R0` in `net1`

```
R0(config)#interface FastEthernet0/0
R0(config-if)#ip address 176.141.64.129 255.255.255.192
```

- `R0` in `net2`

```
R0(config)#interface Serial0/2
R0(config-if)#ip address 176.141.64.193 255.255.255.252
```

- `R1` in `net2`

```
R1(config)#interface Serial0/1
R1(config-if)#ip address 176.141.64.194 255.255.255.252
```

- `R1` in `net3`

```
R1(config)#interface FastEthernet0/0
R1(config-if)#ip address 176.141.64.1 255.255.255.128
```

## task3 - routes

- `R0` -> `net3`

```
R0(config)#ip route 0.0.0.0 0.0.0.0 176.141.64.194
```

- `R1` -> `net1`

```
R1(config)#ip route 0.0.0.0 0.0.0.0 176.141.64.193
```

## task4 - `dhcp` setup

```
R1(config)#ip dhcp pool LAN-address
R1(dhcp-config)#network 176.141.64.0 255.255.255.128
R1(dhcp-config)#ip dhcp excluded-address 176.141.64.1 176.141.64.2
R1(dhcp-config)#ip domain name cisco.com
R1(dhcp-config)#dns-server 176.141.64.2
R1(dhcp-config)#default-router 176.141.64.1
R1(dhcp-config)#exit
R1(config)#exit
```

- `show running-config`:

```
    Current configuration : 931 bytes
    !
    version 12.2
    no service timestamps log datetime msec
    no service timestamps debug datetime msec
    no service password-encryption
    !
    hostname R1
    !
    ip dhcp excluded-address 176.141.64.1 176.141.64.2
    !
    ip dhcp pool LAN-address
     network 176.141.64.0 255.255.255.128
     default-router 176.141.64.1
     dns-server 176.141.64.2
    !
    ip domain-name cisco.com
    !
    interface FastEthernet0/0
     ip address 176.141.64.1 255.255.255.128
     duplex auto
     speed auto
    !
    interface Serial0/1
     ip address 176.141.64.194 255.255.255.252
    !
```

## task5 check routes

### `R0`

- `show ip route`:

```
         176.141.0.0/16 is variably subnetted, 2 subnets, 2 masks
    C       176.141.64.128/26 is directly connected, FastEthernet0/0
    C       176.141.64.192/30 is directly connected, Serial0/2
```

### `R1`

- `show ip route`:

```
         176.141.0.0/16 is variably subnetted, 3 subnets, 3 masks
    C       176.141.64.0/25 is directly connected, FastEthernet0/0
    S       176.141.64.128/26 [1/0] via 176.141.64.193
    C       176.141.64.192/30 is directly connected, Serial0/1
```

## task 6 `dhcp` `pc` addressing

- `PC2`

```
PC>ipconfig

  FastEthernet0 Connection:(default port)

     Link-local IPv6 Address.........: FE80::201:42FF:FE44:D9E0
     IP Address......................: 176.141.64.4
     Subnet Mask.....................: 255.255.255.128
     Default Gateway.................: 176.141.64.1

  PC>ipconfig /release

     IP Address......................: 0.0.0.0
     Subnet Mask.....................: 0.0.0.0
     Default Gateway.................: 0.0.0.0
     DNS Server......................: 0.0.0.0

  PC>ipconfig /renew

     IP Address......................: 176.141.64.3
     Subnet Mask.....................: 255.255.255.128
     Default Gateway.................: 176.141.64.1
     DNS Server......................: 176.141.64.2
```

## task7 - check connection

### `net1` -> `net3` (`PC0` -> `PC2`)

- `ping 176.141.64.3`

```
    Reply from 176.141.64.3: bytes=32 time=1ms TTL=126
    Reply from 176.141.64.3: bytes=32 time=1ms TTL=126
    Reply from 176.141.64.3: bytes=32 time=1ms TTL=126
    Reply from 176.141.64.3: bytes=32 time=2ms TTL=126

    Ping statistics for 176.141.64.3:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 1ms, Maximum = 2ms, Average = 1ms
```

### `net3` -> `net1` (`PC2` -> `PC0`)

- `ping 176.141.64.130`

```
    Pinging 176.141.64.130 with 32 bytes of data:

    Reply from 176.141.64.130: bytes=32 time=1ms TTL=126
    Reply from 176.141.64.130: bytes=32 time=1ms TTL=126
    Reply from 176.141.64.130: bytes=32 time=1ms TTL=126
    Reply from 176.141.64.130: bytes=32 time=1ms TTL=126

    Ping statistics for 176.141.64.130:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 1ms, Maximum = 1ms, Average = 1ms
```

# part2

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491838332/networks9-2.png)

## task1 `dhcp` router config

```
R0(config)#interface FastEthernet0/0
R0(config-if)#ip address 176.141.64.1 255.255.0.0
```

```
R0(config)#ip dhcp pool pool18
R0(dhcp-config)#network 176.141.64.0 255.255.255.0
R0(dhcp-config)#dns-server 176.141.64.18
R0(dhcp-config)#default-router 176.141.64.1
R0(dhcp-config)#ip dhcp excluded-address 176.141.64.1 176.141.64.18
R0(config)#ip domain name bsu.by
R0(config)#end
```

## task2 check config

- `sh run`

```
    !
    hostname R0
    !
    ip dhcp excluded-address 176.141.64.1 176.141.64.18
    !
    ip dhcp pool pool18
     network 176.141.64.0 255.255.255.0
     default-router 176.141.64.1
     dns-server 176.141.64.18
    !
    ip domain name bsu.by
    !
    interface FastEthernet0/0
     ip address 176.141.64.1 255.255.0.0
     duplex auto
     speed auto
    !
```
