# lab6
* *Пажитных Иван Павлович*
* *3 курс, 1 группа, МСС*
* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab6)

## task1 - nets size and adressing
* `net1` ~ `5000`

name | value
--- | ---
ip/mask | `173.213.192.0/19`
ip | `173.213.192.0`
mask | `255.255.224.0`
net size | `8190`
min addr | `173.213.192.1`
max addr | `173.213.223.254`
broadcast | `173.213.223.255`

* `net2` ~ `2000`

name | value
--- | ---
ip/mask | `173.213.224.0/21`
ip | `173.213.224.0`
mask | `255.255.248.0`
net size | `2046`
min addr | `173.213.224.1`
max addr | `173.213.231.254`
broadcast | `173.213.231.255`

* `net3` ~ `1950`

name | value
--- | ---
ip/mask | `173.213.232.0/21`
ip | `173.213.232.0`
mask | `255.255.248.0`
net size | `2046`
min addr | `173.213.232.1`
max addr | `173.213.239.254`
broadcast | `173.213.239.255`

* `net4` ~ `800`

name | value
--- | ---
ip/mask | `173.213.240.0/22`
ip | `173.213.240.0`
mask | `255.255.252.0`
net size | `1022`
min addr | `173.213.240.1`
max addr | `173.213.243.254`
broadcast | `173.213.243.255`

* `net5` ~ `2`

name | value
--- | ---
ip/mask | `173.213.244.0/30`
ip | `173.213.244.0`
mask | `255.255.255.252`
net size | `2`
min addr | `173.213.244.1`
max addr | `173.213.244.2`
broadcast | `173.213.244.3`

* `net6` ~ `2`

name | value
--- | ---
ip/mask | `173.213.244.4/30`
ip | `173.213.244.4`
mask | `255.255.255.252`
net size | `2`
min addr | `173.213.244.5`
max addr | `173.213.244.6`
broadcast | `173.213.244.7`

* `net7` ~ `2`

name | value
--- | ---
ip/mask | `173.213.244.8/30`
ip | `173.213.244.8`
mask | `255.255.255.252`
net size | `2`
min addr | `173.213.244.9`
max addr | `173.213.244.10`
broadcast | `173.213.244.11`

## task2 - build schema
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1490039244/networks-6-1.png)

## task3 - routers and switchs names
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

## task4 - ip configs

* `PC0` in `net1`
```
   Link-local IPv6 Address.........: FE80::2D0:BCFF:FEC7:C1BC
   IP Address......................: 173.213.192.1
   Subnet Mask.....................: 255.255.224.0
   Default Gateway.................: 173.213.192.4
```

* `PC1` in `net1`
```
   Link-local IPv6 Address.........: FE80::290:CFF:FEBA:3B20
   IP Address......................: 173.213.192.2
   Subnet Mask.....................: 255.255.224.0
   Default Gateway.................: 173.213.192.4
```

* `PC2` in `net1`
```
   Link-local IPv6 Address.........: FE80::260:70FF:FE70:A577
   IP Address......................: 173.213.192.3
   Subnet Mask.....................: 255.255.224.0
   Default Gateway.................: 173.213.192.4
```

* `R4` in `net1`
```
R4(config)#interface FastEthernet0/0
R4(config-if)#ip address 173.213.192.4 255.255.224.0
R4(config-if)#no shutdown
R4(config-if)#exit
```

* `PC3` in `net2`
```
   Link-local IPv6 Address.........: FE80::210:11FF:FE8A:2C21
   IP Address......................: 173.213.224.1
   Subnet Mask.....................: 255.255.248.0
   Default Gateway.................: 173.213.224.4
```

* `PC4` in `net2`
```
   Link-local IPv6 Address.........: FE80::260:3EFF:FE48:C5E
   IP Address......................: 173.213.224.2
   Subnet Mask.....................: 255.255.248.0
   Default Gateway.................: 173.213.224.4
```

* `PC5` in `net2`
```
   Link-local IPv6 Address.........: FE80::260:47FF:FE31:C766
   IP Address......................: 173.213.224.3
   Subnet Mask.....................: 255.255.248.0
   Default Gateway.................: 173.213.224.4
```

* `R2` in `net2`
```
R2(config)#interface FastEthernet0/0
R2(config-if)#ip address 173.213.224.4 255.255.248.0
R2(config-if)#no shutdown
R2(config-if)#exit
```

* `PC6` in `net3`
```
   Link-local IPv6 Address.........: FE80::201:96FF:FE12:8E6E
   IP Address......................: 173.213.232.1
   Subnet Mask.....................: 255.255.248.0
   Default Gateway.................: 173.213.232.4
```

* `PC7` in `net3`
```
   Link-local IPv6 Address.........: FE80::202:17FF:FEB4:861
   IP Address......................: 173.213.232.2
   Subnet Mask.....................: 255.255.248.0
   Default Gateway.................: 173.213.232.4
```

* `PC8` in `net3`
```
   Link-local IPv6 Address.........: FE80::2D0:BAFF:FE19:210E
   IP Address......................: 173.213.232.3
   Subnet Mask.....................: 255.255.248.0
   Default Gateway.................: 173.213.232.4
```

* `R3` in `net3`
```
R3(config)#interface FastEthernet0/0
R3(config-if)#ip address 173.213.232.4 255.255.248.0
R3(config-if)#no shutdown
R3(config-if)#exit
```

* `PC9` in `net4`
```
   Link-local IPv6 Address.........: FE80::201:96FF:FE12:8E6E
   IP Address......................: 173.213.240.1
   Subnet Mask.....................: 255.255.252.0
   Default Gateway.................: 173.213.240.4
```

* `PC10` in `net4`
```
   Link-local IPv6 Address.........: FE80::203:E4FF:FE0B:6199
   IP Address......................: 173.213.240.2
   Subnet Mask.....................: 255.255.252.0
   Default Gateway.................: 173.213.240.4
```

* `PC11` in `net4`
```
   Link-local IPv6 Address.........: FE80::260:2FFF:FEB8:47D
   IP Address......................: 173.213.240.3
   Subnet Mask.....................: 255.255.252.0
   Default Gateway.................: 173.213.240.4
```

* `R1` in `net4`
```
R1(config)#interface FastEthernet0/0
R1(config-if)#ip address 173.213.240.4 255.255.252.0
R1(config-if)#no shutdown
R1(config-if)#exit
```

* `R1` in `net5`
```
R1(config)#interface Serial0/0
R1(config-if)#ip address 173.213.244.1 255.255.255.252
R1(config-if)#no shutdown
R1(config-if)#exit
```

* `R3` in `net5`
```
R3(config)#interface Serial0/3
R3(config-if)#ip address 173.213.244.2 255.255.255.252
R3(config-if)#no shutdown
R3(config-if)#exit
```

* `R2` in `net6`
```
R2(config)#interface Serial0/0
R2(config-if)#ip address 173.213.244.5 255.255.255.252
R2(config-if)#no shutdown
R2(config-if)#exit
```

* `R3` in `net6`
```
R3(config)#interface Serial0/0
R3(config-if)#ip address 173.213.244.6 255.255.255.252
R3(config-if)#no shutdown
R3(config-if)#exit
```

* `R4` in `net7`
```
R4(config)#interface Serial0/0
R4(config-if)#ip address 173.213.244.9 255.255.255.252
R4(config-if)#no shutdown
R4(config-if)#exit
```

* `R3` in `net7`
```
R3(config)#interface Serial0/2
R3(config-if)#ip address 173.213.244.10 255.255.255.252
R3(config-if)#no shutdown
R3(config-if)#exit
```

## task5 - static routes
* set routes from `R1` to `net1`, `net2`, `net3` via `R3` :
```
R1(config)#ip route 173.213.192.0 255.255.224.0 173.213.244.2
R1(config)#ip route 173.213.224.0 255.255.248.0 173.213.244.2
R1(config)#ip route 173.213.232.0 255.255.248.0 173.213.244.2
```

* `show ip route` for `R1`
```
        173.213.0.0/16 is variably subnetted, 5 subnets, 4 masks
   S       173.213.192.0/19 [1/0] via 173.213.244.2
   S       173.213.224.0/21 [1/0] via 173.213.244.2
   S       173.213.232.0/21 [1/0] via 173.213.244.2
   C       173.213.240.0/22 is directly connected, FastEthernet0/0
   C       173.213.244.0/30 is directly connected, Serial0/0
```

* set routes from `R2` to `net1`, `net3`, `net4` via `R3`:
```
R2(config)#ip route 173.213.192.0 255.255.224.0 173.213.244.6
R2(config)#ip route 173.213.232.0 255.255.248.0 173.213.244.6
R2(config)#ip route 173.213.240.0 255.255.252.0 173.213.244.6
```

* `show ip route` for `R2`
```
        173.213.0.0/16 is variably subnetted, 5 subnets, 4 masks
   S       173.213.192.0/19 [1/0] via 173.213.244.6
   C       173.213.224.0/21 is directly connected, FastEthernet0/0
   S       173.213.232.0/21 [1/0] via 173.213.244.6
   S       173.213.240.0/22 [1/0] via 173.213.244.6
   C       173.213.244.4/30 is directly connected, Serial0/0
```

* set routes from `R4` to `net2`, `net3`, `net4` via `R3`:
```
R4(config)#ip route 173.213.224.0 255.255.248.0 173.213.244.10
R4(config)#ip route 173.213.232.0 255.255.248.0 173.213.244.10
R4(config)#ip route 173.213.240.0 255.255.252.0 173.213.244.10
```

* `show ip route` for `R2`
```
        173.213.0.0/16 is variably subnetted, 5 subnets, 4 masks
   C       173.213.192.0/19 is directly connected, FastEthernet0/0
   S       173.213.224.0/21 [1/0] via 173.213.244.10
   S       173.213.232.0/21 [1/0] via 173.213.244.10
   S       173.213.240.0/22 [1/0] via 173.213.244.10
   C       173.213.244.8/30 is directly connected, Serial0/0
```

* set routes from `R3` to `net1`, `net2`, `net4` via `R4`, `R2` and `R1` respectively:
```
R3(config)#ip route 173.213.192.0 255.255.224.0 173.213.244.9
R3(config)#ip route 173.213.224.0 255.255.248.0 173.213.244.5
R3(config)#ip route 173.213.240.0 255.255.252.0 173.213.244.1
```

* `show ip route` for `R3`
```
        173.213.0.0/16 is variably subnetted, 7 subnets, 4 masks
   S       173.213.192.0/19 [1/0] via 173.213.244.9
   S       173.213.224.0/21 [1/0] via 173.213.244.5
   C       173.213.232.0/21 is directly connected, FastEthernet0/0
   S       173.213.240.0/22 [1/0] via 173.213.244.1
   C       173.213.244.0/30 is directly connected, Serial0/3
   C       173.213.244.4/30 is directly connected, Serial0/0
   C       173.213.244.8/30 is directly connected, Serial0/2
```

## task6 - check connection
### `net1` -> `net2` (`PC0` -> `PC3`)
* `ping 173.213.224.1`
```
   Ping statistics for 173.213.224.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 10ms, Average = 6ms
```

### `net1` -> `net3` (`PC0` -> `PC7`)
* `ping 173.213.232.2`
```
   Ping statistics for 173.213.232.2:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 1ms, Maximum = 2ms, Average = 1ms
```

### `net1` -> `net4` (`PC1` -> `PC11`)
* `ping 173.213.240.3`
```
   Ping statistics for 173.213.240.3:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 7ms, Average = 3ms
```

### `net4` -> `net2` (`PC10` -> `PC5`)
* `ping 173.213.224.3`
```
   Ping statistics for 173.213.224.3:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 2ms, Maximum = 10ms, Average = 7ms
```

### `net3` -> `net1` (`PC6` -> `PC0`)
* `ping 173.213.192.1`
```
   Ping statistics for 173.213.192.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 1ms, Maximum = 9ms, Average = 3ms
```

and so on, all conections work fine!