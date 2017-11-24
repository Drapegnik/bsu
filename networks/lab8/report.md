# lab8

* _Пажитных Иван Павлович_
* _3 курс, 1 группа, МСС_
* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab8)

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1490803121/tp-lab7.png)

## task1 - routers and switchs names

```
Router>enable
Router#config t
Router(config)#hostname R1
```

```
Switch>enable
Switch#config t
Switch(config)#hostname S0
```

do same with `R2`, `R3`, `S1`, `S2`, `S3`

## task2 - ip configs

* `PC0` in `net5`

```
   Link-local IPv6 Address.........: FE80::202:17FF:FEB8:6208
   IP Address......................: 175.123.5.1
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 175.123.5.2
```

* `PC1` in `net6`

```
   Link-local IPv6 Address.........: FE80::204:9AFF:FE68:5CD5
   IP Address......................: 175.123.6.1
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 175.123.6.2
```

* `PC2` in `net4`

```
   Link-local IPv6 Address.........: FE80::201:43FF:FE63:99CB
   IP Address......................: 175.123.4.1
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 175.123.4.2
```

* `R0` in `net5`

```
R0(config)#interface FastEthernet0/0
R0(config-if)#ip address 175.123.5.2 255.255.255.0
```

* `R0` in `net1`

```
R0(config)#interface Serial0/2
R0(config-if)#ip address 175.123.1.2 255.255.255.0
```

* `R0` in `net2`

```
R0(config)#interface Serial0/0
R0(config-if)#ip address 175.123.2.1 255.255.255.0
```

* `R1` in `net6`

```
R1(config)#interface FastEthernet0/0
R1(config-if)#ip address 175.123.6.2 255.255.255.0
```

* `R1` in `net2`

```
R1(config)#interface Serial0/2
R1(config-if)#ip address 175.123.2.2 255.255.255.0
```

* `R1` in `net3`

```
R1(config)#interface Serial0/0
R1(config-if)#ip address 175.123.3.1 255.255.255.0
```

* `R2` in `net4`

```
R2(config)#interface FastEthernet0/0
R2(config-if)#ip address 175.123.4.2 255.255.255.0
```

* `R2` in `net1`

```
R2(config)#interface Serial0/2
R2(config-if)#ip address 175.123.1.1 255.255.255.0
```

* `R2` in `net3`

```
R2(config)#interface Serial0/0
R2(config-if)#ip address 175.123.3.2 255.255.255.0
```

## task3 - _OSPF_ routes config

* `R0`

```
R0(config)#router ospf 1
R0(config-router)#network 175.123.5.0 0.0.0.255 area 18
R0(config-router)#network 175.123.1.0 0.0.0.255 area 18
R0(config-router)#network 175.123.2.0 0.0.0.255 area 18
```

* `R1`

```
R1(config)#router ospf 1
R1(config-router)#network 175.123.6.0 0.0.0.255 area 18
R1(config-router)#network 175.123.2.0 0.0.0.255 area 18
R1(config-router)#network 175.123.3.0 0.0.0.255 area 18
```

* `R2`

```
R2(config)#router ospf 1
R2(config-router)#network 175.123.4.0 0.0.0.255 area 18
R2(config-router)#network 175.123.1.0 0.0.0.255 area 18
R2(config-router)#network 175.123.3.0 0.0.0.255 area 18
```

## task4 - check routes

### `R0`

* `show ip route`:

```
         175.123.0.0/24 is subnetted, 6 subnets
    C       175.123.1.0 is directly connected, Serial0/2
    C       175.123.2.0 is directly connected, Serial0/0
    O       175.123.3.0 [110/128] via 175.123.1.1, 00:01:56, Serial0/2
                        [110/128] via 175.123.2.2, 00:01:56, Serial0/0
    O       175.123.4.0 [110/65] via 175.123.1.1, 00:01:56, Serial0/2
    C       175.123.5.0 is directly connected, FastEthernet0/0
    O       175.123.6.0 [110/65] via 175.123.2.2, 00:03:07, Serial0/0
```

### `R1`

* `show ip route`:

```
         175.123.0.0/24 is subnetted, 6 subnets
    O       175.123.1.0 [110/128] via 175.123.3.2, 00:00:05, Serial0/0
                        [110/128] via 175.123.2.1, 00:00:05, Serial0/2
    C       175.123.2.0 is directly connected, Serial0/2
    C       175.123.3.0 is directly connected, Serial0/0
    O       175.123.4.0 [110/65] via 175.123.3.2, 00:03:48, Serial0/0
    O       175.123.5.0 [110/65] via 175.123.2.1, 00:00:05, Serial0/2
    C       175.123.6.0 is directly connected, FastEthernet0/0
```

### `R2`

* `show ip route`:

```
         175.123.0.0/24 is subnetted, 6 subnets
    C       175.123.1.0 is directly connected, Serial0/2
    O       175.123.2.0 [110/128] via 175.123.1.2, 00:00:25, Serial0/2
                        [110/128] via 175.123.3.1, 00:00:25, Serial0/0
    C       175.123.3.0 is directly connected, Serial0/0
    C       175.123.4.0 is directly connected, FastEthernet0/0
    O       175.123.5.0 [110/65] via 175.123.1.2, 00:04:23, Serial0/2
    O       175.123.6.0 [110/65] via 175.123.3.1, 00:04:23, Serial0/0
```

## task5 - get routers `id`

### `R0`

* `show ip protocols`:

```
    Routing Protocol is "ospf 1"
      Outgoing update filter list for all interfaces is not set
      Incoming update filter list for all interfaces is not set
      Router ID 175.123.5.2
      Number of areas in this router is 1. 1 normal 0 stub 0 nssa
      Maximum path: 4
      Routing for Networks:
        175.123.5.0 0.0.0.255 area 18
        175.123.1.0 0.0.0.255 area 18
        175.123.2.0 0.0.0.255 area 18
      Routing Information Sources:
        Gateway         Distance      Last Update
        175.123.4.2          110      00:07:31
        175.123.5.2          110      00:03:33
        175.123.6.2          110      00:03:33
      Distance: (default is 110)
```

### `R1`

* `show ip protocols`:

```
    Routing Protocol is "ospf 1"
      Outgoing update filter list for all interfaces is not set
      Incoming update filter list for all interfaces is not set
      Router ID 175.123.6.2
      Number of areas in this router is 1. 1 normal 0 stub 0 nssa
      Maximum path: 4
      Routing for Networks:
        175.123.6.0 0.0.0.255 area 18
        175.123.2.0 0.0.0.255 area 18
        175.123.3.0 0.0.0.255 area 18
      Routing Information Sources:
        Gateway         Distance      Last Update
        175.123.4.2          110      00:08:07
        175.123.5.2          110      00:04:10
        175.123.6.2          110      00:04:10
      Distance: (default is 110)
```

### `R2`

* `show ip protocols`:

```
    Routing Protocol is "ospf 1"
      Outgoing update filter list for all interfaces is not set
      Incoming update filter list for all interfaces is not set
      Router ID 175.123.4.2
      Number of areas in this router is 1. 1 normal 0 stub 0 nssa
      Maximum path: 4
      Routing for Networks:
        175.123.4.0 0.0.0.255 area 18
        175.123.1.0 0.0.0.255 area 18
        175.123.3.0 0.0.0.255 area 18
      Routing Information Sources:
        Gateway         Distance      Last Update
        175.123.4.2          110      00:08:25
        175.123.5.2          110      00:04:28
        175.123.6.2          110      00:04:28
      Distance: (default is 110)
```

## task6 - check neighbors

### `R0`

* `show ip ospf neighbor`:

```
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    175.123.6.2       0   FULL/  -        00:00:31    175.123.2.2     Serial0/0
    175.123.4.2       0   FULL/  -        00:00:39    175.123.1.1     Serial0/2
```

### `R1`

* `show ip ospf neighbor`:

```
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    175.123.5.2       0   FULL/  -        00:00:35    175.123.2.1     Serial0/2
    175.123.4.2       0   FULL/  -        00:00:34    175.123.3.2     Serial0/0
```

### `R2`

* `show ip ospf neighbor`:

```
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    175.123.6.2       0   FULL/  -        00:00:37    175.123.3.1     Serial0/0
    175.123.5.2       0   FULL/  -        00:00:37    175.123.1.2     Serial0/2
```

## task7 - routers cost

### `R1`

* `ip ospf cost`:

```
R1(config)#interface serial 0/0
R1(config-if)#ip ospf cost 2000
R1(config-if)#no shutdown
R1(config-if)#exit
R1(config)#interface serial 0/2
R1(config-if)#ip ospf cost 2000
R1(config-if)#no shutdown
R1(config-if)#exit
```

* `show ip ospf interface`:

```
  Serial0/0 is up, line protocol is up
    Internet address is 175.123.3.1/24, Area 18
    Process ID 1, Router ID 175.123.6.2, Network Type POINT-TO-POINT, Cost: 2000
    Transmit Delay is 1 sec, State POINT-TO-POINT, Priority 0
    No designated router on this network
    No backup designated router on this network
    Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
      Hello due in 00:00:00
    Index 2/2, flood queue length 0
    Next 0x0(0)/0x0(0)
    Last flood scan length is 1, maximum is 1
    Last flood scan time is 0 msec, maximum is 0 msec
    Neighbor Count is 1 , Adjacent neighbor count is 1
      Adjacent with neighbor 175.123.4.2
    Suppress hello for 0 neighbor(s)
```

```
  Serial0/2 is up, line protocol is up
    Internet address is 175.123.2.2/24, Area 18
    Process ID 1, Router ID 175.123.6.2, Network Type POINT-TO-POINT, Cost: 2000
    Transmit Delay is 1 sec, State POINT-TO-POINT, Priority 0
    No designated router on this network
    No backup designated router on this network
    Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
      Hello due in 00:00:06
    Index 3/3, flood queue length 0
    Next 0x0(0)/0x0(0)
    Last flood scan length is 1, maximum is 1
    Last flood scan time is 0 msec, maximum is 0 msec
    Neighbor Count is 1 , Adjacent neighbor count is 1
      Adjacent with neighbor 175.123.5.2
    Suppress hello for 0 neighbor(s)
```

as we can see above, cost set to `2000`

## task8 - check connection

### `net5` -> `net6` (`PC0` -> `PC1`)

* `ping 175.123.5.1`

```
   Ping statistics for 175.123.5.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 10ms, Average = 6ms
```

### `net5` -> `net4` (`PC0` -> `PC2`)

* `ping 175.123.4.1`

```
   Ping statistics for 175.123.4.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 11ms, Average = 5ms
```

* `tracert 175.123.4.1`:

```
    Tracing route to 175.123.4.1 over a maximum of 30 hops:
      1   0 ms      0 ms      0 ms      175.123.5.2
      2   1 ms      1 ms      0 ms      175.123.1.1
      3   1 ms      1 ms      0 ms      175.123.4.1
    Trace complete.
```

### `net4` -> `net6` (`PC2` -> `PC1`)

* `ping 175.123.6.1`

```
    Ping statistics for 175.123.6.1:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 1ms, Maximum = 8ms, Average = 2ms
```

* `tracert 175.123.6.1`:

```
    Tracing route to 175.123.6.1 over a maximum of 30 hops:
      1   1 ms      0 ms      0 ms      175.123.4.2
      2   1 ms      0 ms      1 ms      175.123.3.1
      3   0 ms      1 ms      1 ms      175.123.6.1
    Trace complete.
```

### `net4` -> `net5` (`PC2` -> `PC0`)

* `ping 175.123.5.1`

```
   Ping statistics for 175.123.5.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 8ms, Average = 4ms
```

* `tracert 175.123.5.1`:

```
    Tracing route to 175.123.5.1 over a maximum of 30 hops:
      1   1 ms      0 ms      0 ms      175.123.4.2
      2   0 ms      1 ms      1 ms      175.123.1.2
      3   0 ms      1 ms      1 ms      175.123.5.1
    Trace complete.
```

and so on, all conections work fine!

## task 9 connection stability

* switch off `serial 0/0` for `R2`:
  ```
  R2(config)#interface Serial0/0
  R2(config-if)#shutdown
  ```
* check connection `net4` -> `net6` (`PC2` -> `PC1`)

  * `tracert 175.123.6.1`:

  ```
    Tracing route to 175.123.6.1 over a maximum of 30 hops:
      1   0 ms      0 ms      0 ms      175.123.4.2
      2   1 ms      0 ms      0 ms      175.123.1.2
      3   1 ms      2 ms      0 ms      175.123.2.2
      4   1 ms      0 ms      2 ms      175.123.6.1
    Trace complete.
  ```

* check connection `net6` -> `net4` (`PC1` -> `PC2`)
  * `tracert 175.123.4.1`:
  ```
    Tracing route to 175.123.4.1 over a maximum of 30 hops:
      1   1 ms      0 ms      0 ms      175.123.6.2
      2   1 ms      0 ms      0 ms      175.123.2.1
      3   0 ms      1 ms      1 ms      175.123.1.1
      4   0 ms      1 ms      2 ms      175.123.4.1
    Trace complete.
  ```

as we can see above, connection doesn't lost, but used another ways for routing
(across router `R0`)
