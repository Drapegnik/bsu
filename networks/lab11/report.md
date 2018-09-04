# lab11

- _Пажитных Иван Павлович_
- _3 курс, 1 группа, МСС_
- [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab11)

## task0 - schema

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1494851136/networks-11-2.png)

## task1 - ip configs

- `PC1`:

```
   Link-local IPv6 Address.........: FE80::260:2FFF:FE42:BC29
   IP Address......................: 10.162.140.3
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 10.162.140.1
```

- `PC2`:

```
   Link-local IPv6 Address.........: FE80::204:9AFF:FEAB:C88
   IP Address......................: 10.162.140.2
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 10.162.140.1
```

- `Gateway`:

```
Gateway#config tGateway(config)#interface fast
Gateway(config)#interface fastEthernet0/0
Gateway(config-if)#ip address 10.162.140.1 255.255.255.0
Gateway(config-if)#exit
```

```
Gateway(config)#interface serial0/1
Gateway(config-if)#ip address 176.141.0.1 255.255.255.252
Gateway(config-if)#exit
```

- `ISP`:

```
ISP(config)#interface serial0/1
ISP(config-if)#ip address 176.141.0.2 255.255.255.252
```

```
ISP(config)#interface loopback1
ISP(config-if)#ip address 172.16.1.18 255.255.255.255
```

## task2 - connection check & QA

### `PC1` -> `Gateway`:

- `ping 10.162.140.1`

```
	Reply from 10.162.140.1: bytes=32 time=2ms TTL=255
	Reply from 10.162.140.1: bytes=32 time=0ms TTL=255
	Reply from 10.162.140.1: bytes=32 time=0ms TTL=255
	Reply from 10.162.140.1: bytes=32 time=0ms TTL=255
	Ping statistics for 10.162.140.1:
	    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
	Approximate round trip times in milli-seconds:
	    Minimum = 0ms, Maximum = 2ms, Average = 0ms
```

### `PC2` -> `Gateway`:

- `ping 10.162.140.1`

```
	Reply from 10.162.140.1: bytes=32 time=1ms TTL=255
	Reply from 10.162.140.1: bytes=32 time=0ms TTL=255
	Reply from 10.162.140.1: bytes=32 time=1ms TTL=255
	Reply from 10.162.140.1: bytes=32 time=0ms TTL=255
	Ping statistics for 10.162.140.1:
	    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
	Approximate round trip times in milli-seconds:
	    Minimum = 0ms, Maximum = 1ms, Average = 0ms
```

> Если бы вы попытались отправить эхо-запросы на _IP_-адрес маршрутизатора
> `ISP`, был бы этот эхо-запрос успешным? Поясните свой ответ.

> Ответ: результат был бы не успешным, т.к. не настроена маршрутизация на
> `Gateway`

## task3 - routes config

### `Gateway`:

- default gateway:

```
Gateway(config)#ip route 0.0.0.0 0.0.0.0 176.141.0.2
```

- `show ip route`:

```
	Gateway of last resort is 176.141.0.2 to network 0.0.0.0
	     10.0.0.0/24 is subnetted, 1 subnets
	C       10.162.140.0 is directly connected, FastEthernet0/0
	     176.141.0.0/30 is subnetted, 1 subnets
	C       176.141.0.0 is directly connected, Serial0/1
	S*   0.0.0.0/0 [1/0] via 176.141.0.2
```

#### `PC1` -> `ISP`

- `ping 176.141.0.2`:

```
	Request timed out.
	Request timed out.
	Request timed out.
	Request timed out.
	Ping statistics for 176.141.0.2:
	    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
```

### `ISP`

- static route:

```
ISP(config)#ip route 10.162.140.0 255.255.255.0 176.141.0.1
```

#### `PC1` -> `ISP`

- `ping 176.141.0.2`:

```
	Reply from 176.141.0.2: bytes=32 time=5ms TTL=255
	Reply from 176.141.0.2: bytes=32 time=7ms TTL=255
	Reply from 176.141.0.2: bytes=32 time=4ms TTL=255
	Reply from 176.141.0.2: bytes=32 time=6ms TTL=255
	Ping statistics for 176.141.0.2:
	    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
	Approximate round trip times in milli-seconds:
	    Minimum = 5ms, Maximum = 7ms, Average = 6ms
```

## task4 - _NAT_ config

- `Gateway`:

```
Gateway(config)#ip nat pool public_access 176.141.0.1 176.141.0.1 netmask 255.255.255.252
Gateway(config)#access-list 1 permit 10.162.140.0 0.0.0.255
Gateway(config)#ip nat inside source list 1 pool public_access overload
Gateway(config)#interface fastethernet 0/0
Gateway(config-if)#ip nat inside
Gateway(config-if)#interface serial 0/0
Gateway(config-if)#ip nat outside
Gateway(config-if)#exit
```

## task5 - generate traffic

### `PC1` -> `loopback`:

- `ping 172.16.1.18`:

```
Reply from 172.16.1.18: bytes=32 time=94ms TTL=254
Reply from 172.16.1.18: bytes=32 time=94ms TTL=254
Reply from 172.16.1.18: bytes=32 time=80ms TTL=254
Reply from 172.16.1.18: bytes=32 time=94ms TTL=254

Ping statistics for 172.16.1.18:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 80ms, Maximum = 94ms, Average = 90ms
```

### `PC2` -> `loopback`:

- `ping 172.16.1.18`:

```
Reply from 172.16.1.18: bytes=32 time=93ms TTL=254
Reply from 172.16.1.18: bytes=32 time=93ms TTL=254
Reply from 172.16.1.18: bytes=32 time=94ms TTL=254
Reply from 172.16.1.18: bytes=32 time=93ms TTL=254

Ping statistics for 172.16.1.18:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 93ms, Maximum = 94ms, Average = 93ms
```

## task6 - check `NAT`

### Gateway

- `show ip nat statistics`

```
	Total translations: 0 (0 static, 0 dynamic, 0 extended)
	Outside Interfaces: Serial0/0
	Inside Interfaces: FastEthernet0/0
	Hits: 8  Misses: 8
	Expired translations: 8
	Dynamic mappings:
	-- Inside Source
	access-list 1 pool public_access refCount 0
	 pool public_access: netmask 255.255.255.252
	       start 176.141.0.1 end 176.141.0.1
	       type generic, total addresses 1 , allocated 0 (0%), misses 0
```
