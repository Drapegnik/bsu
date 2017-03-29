# lab7
* *Пажитных Иван Павлович*
* *3 курс, 1 группа, МСС*
* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab7)

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

## task3 - *RIP* `v2` config
* `R0`
```
R0(config)#router rip
R0(config-router)#version 2
R0(config-router)#network 175.123.5.0
R0(config-router)#network 175.123.1.0
R0(config-router)#network 175.123.2.0
```

* `R1`
```
R1(config)#router rip
R1(config-router)#version 2
R1(config-router)#network 175.123.6.0
R1(config-router)#network 175.123.2.0
R1(config-router)#network 175.123.3.0
```

* `R2`
```
R2(config)#router rip
R2(config-router)#version 2
R2(config-router)#network 175.123.4.0
R2(config-router)#network 175.123.1.0
R2(config-router)#network 175.123.3.0
```

## task4 - check protocols and routes

### `R0`

* `show ip protocols`:
```
  Maximum path: 4
  Routing for Networks:
    175.123.0.0
  Passive Interface(s):
    FastEthernet0/0
  Routing Information Sources:
    Gateway         Distance      Last Update
    175.123.2.2          120      00:00:05
    175.123.1.1          120      00:00:07
  Distance: (default is 120)
```

* `show ip route`:
```
       175.123.0.0/24 is subnetted, 6 subnets
  C       175.123.1.0 is directly connected, Serial0/2
  C       175.123.2.0 is directly connected, Serial0/0
  R       175.123.3.0 [120/1] via 175.123.2.2, 00:00:19, Serial0/0
                      [120/1] via 175.123.1.1, 00:00:20, Serial0/2
  R       175.123.4.0 [120/1] via 175.123.1.1, 00:00:20, Serial0/2
  C       175.123.5.0 is directly connected, FastEthernet0/0
  R       175.123.6.0 [120/1] via 175.123.2.2, 00:00:19, Serial0/0
```

### `R1`

* `show ip protocols`:
```
  Maximum path: 4
  Routing for Networks:
    175.123.0.0
  Passive Interface(s):
    FastEthernet0/0
  Routing Information Sources:
    Gateway         Distance      Last Update
    175.123.2.1          120      00:00:06
    175.123.3.2          120      00:00:25
  Distance: (default is 120)
```

* `show ip route`:
```
       175.123.0.0/24 is subnetted, 6 subnets
  R       175.123.1.0 [120/1] via 175.123.2.1, 00:00:24, Serial0/2
                      [120/1] via 175.123.3.2, 00:00:13, Serial0/0
  C       175.123.2.0 is directly connected, Serial0/2
  C       175.123.3.0 is directly connected, Serial0/0
  R       175.123.4.0 [120/1] via 175.123.3.2, 00:00:13, Serial0/0
  R       175.123.5.0 [120/1] via 175.123.2.1, 00:00:24, Serial0/2
  C       175.123.6.0 is directly connected, FastEthernet0/0
```

### `R2`

* `show ip protocols`:
```
  Maximum path: 4
  Routing for Networks:
    175.123.0.0
  Passive Interface(s):
    FastEthernet0/0
  Routing Information Sources:
    Gateway         Distance      Last Update
    175.123.3.1          120      00:00:12
    175.123.1.2          120      00:00:16
  Distance: (default is 120)
```

* `show ip route`:
```
       175.123.0.0/24 is subnetted, 6 subnets
  C       175.123.1.0 is directly connected, Serial0/2
  R       175.123.2.0 [120/1] via 175.123.3.1, 00:00:01, Serial0/0
                      [120/1] via 175.123.1.2, 00:00:08, Serial0/2
  C       175.123.3.0 is directly connected, Serial0/0
  C       175.123.4.0 is directly connected, FastEthernet0/0
  R       175.123.5.0 [120/1] via 175.123.1.2, 00:00:08, Serial0/2
  R       175.123.6.0 [120/1] via 175.123.3.1, 00:00:01, Serial0/0
```

## task5 - set passive interface
* `R0`:
```
R0(config)#router rip
R0(config-router)#version 2
R0(config-router)#passive-interface FastEthernet 0/0
```

* `R1`:
```
R1(config)#router rip
R1(config-router)#version 2
R1(config-router)#passive-interface FastEthernet 0/0
```

* `R2`:
```
R2(config)#router rip
R2(config-router)#version 2
R2(config-router)#passive-interface FastEthernet 0/0
```

## task6 - check connection
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

### `net4` -> `net6` (`PC2` -> `PC1`)
* `ping 175.123.6.1`
```
   Ping statistics for 175.123.6.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 11ms, Average = 5ms
```

### `net6` -> `net5` (`PC2` -> `PC0`)
* `ping 175.123.5.1`
```
   Ping statistics for 175.123.5.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 8ms, Average = 4ms
```

and so on, all conections work fine!