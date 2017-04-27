# lab9
* *Пажитных Иван Павлович*
* *3 курс, 1 группа, МСС*
* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab10)

## task1 - nets:

* `net1`:

name | value
--- | ---
ip/mask | `176.141.64.0/26`
ip | `176.141.64.0`
mask | `255.255.255.192`
net size | `62`
min addr | `176.141.64.1`
max addr | `176.141.64.62`
broadcast | `176.141.64.63`

* `net2`:

name | value
--- | ---
ip/mask | `176.141.0.0/26`
ip | `176.141.0.0`
mask | `255.255.255.192`
net size | `62`
min addr | `176.141.0.1`
max addr | `176.141.0.62`
broadcast | `176.141.0.63`

* `net3`:

name | value
--- | ---
ip/mask | `176.141.128.0/26`
ip | `176.141.128.0`
mask | `255.255.255.192`
net size | `62`
min addr | `176.141.128.1`
max addr | `176.141.128.62`
broadcast | `176.141.128.63`

## task2 - schema:

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1493331924/tp-lab10-2.png)

## task3 - ip configs:
### `net1`:

* `PC-64-3`
```
   Link-local IPv6 Address.........: FE80::201:43FF:FE8D:D82
   IP Address......................: 176.141.64.3
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.64.1
```

* `PC-64-4`
```
   Link-local IPv6 Address.........: FE80::20A:F3FF:FE46:638D
   IP Address......................: 176.141.64.4
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.64.1
```

* `PC-64-5`
```
   Link-local IPv6 Address.........: FE80::260:3EFF:FEB4:E130
   IP Address......................: 176.141.64.5
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.64.1
```

* `PC-64-6`
```
   Link-local IPv6 Address.........: FE80::230:A3FF:FE0D:862C
   IP Address......................: 176.141.64.6
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.64.1
```

### `net2`:

* `PC-0-3`
```
   Link-local IPv6 Address.........: FE80::201:96FF:FE60:215D
   IP Address......................: 176.141.0.3
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.0.1
```

* `PC-0-4`
```
   Link-local IPv6 Address.........: FE80::260:2FFF:FE98:DE11
   IP Address......................: 176.141.0.4
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.0.1
```

### `net3`:

* `PC-128-3`
```
   Link-local IPv6 Address.........: FE80::206:2AFF:FE82:4C16
   IP Address......................: 176.141.128.3
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.128.1
```

* `PC-128-4`
```
   Link-local IPv6 Address.........: FE80::2D0:BCFF:FE6D:EAE2
   IP Address......................: 176.141.128.4
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: 176.141.128.1
```

## task4 - switch vlan config:

* `net1`:
```
S0(config)#interface vlan1
S0(config-if)#ip addres 176.141.64.2 255.255.255.192
S0(config-if)#no shutdown
```

* `net2` & `net3`:
```
S0(config)#vlan 10
S0(config-vlan)#exit
S0(config)#vlan 10
S0(config-vlan)#name Students-141-0
S0(config-vlan)#exit
S0(config)#vlan 20
S0(config-vlan)#name Faculty-141-128
S0(config-vlan)#exit
```

* default gateway: `ip default-gateway 176.141.64.1`

* `Fa0/5` & `Fa0/6` to `VLAN 10`:
```
S0(config)#interface FastEthernet0/5
S0(config-if)#switchport mode access
S0(config-if)#switchport access vlan 10
S0(config-if)#interface FastEthernet0/6
S0(config-if)#switchport mode access
S0(config-if)#switchport access vlan 10
```

* `Fa0/7` & `Fa0/8` to `VLAN 20`:
```
S0(config)#interface FastEthernet0/7
S0(config-if)#switchport mode access
S0(config-if)#switchport access vlan 20
S0(config-if)#interface FastEthernet0/8
S0(config-if)#switchport mode access
S0(config-if)#switchport access vlan 20
```

* save configs: `S0#copy running-config startup-config`

* `show vlan brief`:
```
	VLAN Name                             Status    Ports
	---- -------------------------------- --------- -------------------------------
	1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
	                                                Fa0/10, Fa0/11, Fa0/12, Fa0/13
	                                                Fa0/14, Fa0/15, Fa0/16, Fa0/17
	                                                Fa0/18, Fa0/19, Fa0/20, Fa0/21
	                                                Fa0/22, Fa0/23, Fa0/24, Gig0/1
	                                                Gig0/2
	10   Students-141-0                   active    Fa0/5, Fa0/6
	20   Faculty-141-128                  active    Fa0/7, Fa0/8   
	1002 fddi-default                     active    
	1003 token-ring-default               active    
	1004 fddinet-default                  active    
	1005 trnet-default                    active   
```

## task5 - quiz answers:

1. *Все ли другие порты коммутатора расположены во VLAN 1?* - **Нет.**
2. *Какие порты коммутатора расположены во VLAN 10?* - **FastEthernet0/5, FastEthernet0/6.**
3. *Какие порты коммутатора расположены во VLAN 20?* - **FastEthernet0/7, FastEthernet0/8.**
4. *Выполните эхо-запрос с ПК на коммутатор с адресом 176.141.64.2*
	* `ping 176.141.64.2` from `PC-64-3`:
	```
		Ping statistics for 176.141.64.2:
		    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
		Approximate round trip times in milli-seconds:
		    Minimum = 0ms, Maximum = 0ms, Average = 0ms
	```
	
	* `ping 176.141.64.2` from `PC-0-3`:
	```
		Ping statistics for 176.141.64.2:
	    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
	```
	
	* `ping 176.141.64.2` from `PC-128-3`:
	```
		Ping statistics for 176.141.64.2:
	    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
	```
5. *Выполните эхо-запрос с `PC-64-3` на `PC-0-4` и `PC-128-4`*
	* `ping 176.141.0.4` from `PC-64-3`:
	```
		Ping statistics for 176.141.0.4:
	    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
	```
	
	* `ping 176.141.128.4` from `PC-64-3`:
	```
		Ping statistics for 176.141.128.4:
	    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
	```
6. **`PC-64-3` может установить связь с коммутатором (`S0`), а с `PC-0-4` и `PC-128-4`  - нет, так как для коммутатора был установлен шлюз по умолчанию `176.141.64.1`**
7. **Компьютеры не могут установить связь друг с другом, так как не настроена маршрутизация между `S0` и `net2`, `net3`**

## task6 - router config

* switch to router config:
```
S0(config)#interface FastEthernet0/9
S0(config-if)#switchport mode trunk
```

* `R0` in `net1`:
```
R0(config)#interface FastEthernet0/0
R0(config-if)#ip address 176.141.64.1 255.255.255.192
R0(config-if)#no shutdown
R0(config-if)#exit
```

* `R0` in `net2`:
```
R0(config)#interface FastEthernet0/0.10
R0(config-subif)#encapsulation dot1q 10
R0(config-subif)#ip address 176.141.0.1 255.255.255.192
R0(config-subif)#exit
```

* `R0` in `net3`:
```
R0(config)#interface FastEthernet0/0.20
R0(config-subif)#encapsulation dot1q 20
R0(config-subif)#ip address 176.141.128.1 255.255.255.192
R0(config-subif)#exit
```

## task7 - check router configs

* `S0#show interfaces trunk`:
```
	Port        Mode         Encapsulation  Status        Native vlan
	Fa0/9       on           802.1q         trunking      1

	Port        Vlans allowed on trunk
	Fa0/9       1-1005

	Port        Vlans allowed and active in management domain
	Fa0/9       1,10,20

	Port        Vlans in spanning tree forwarding state and not pruned
	Fa0/9       1,10,20
```

* `R0#show ip interface`:
```
	FastEthernet0/0 is up, line protocol is up (connected)
	  Internet address is 176.141.64.1/26
	  Broadcast address is 255.255.255.255
	  Address determined by setup command
	  MTU is 1500 bytes
	FastEthernet0/0.10 is up, line protocol is up (connected)
	  Internet address is 176.141.0.1/26
	  Broadcast address is 255.255.255.255
	  Address determined by setup command
	  MTU is 1500 bytes
	FastEthernet0/0.20 is up, line protocol is up (connected)
	  Internet address is 176.141.128.1/26
	  Broadcast address is 255.255.255.255
	  Address determined by setup command
	  MTU is 1500 bytes
	FastEthernet0/1 is administratively down, line protocol is down (disabled)
	  Internet protocol processing disabled
	Vlan1 is administratively down, line protocol is down
	  Internet protocol processing disabled
```

* `R0#show ip interface brief`:
```
	Interface              IP-Address      OK? Method Status                Protocol
	FastEthernet0/0        176.141.64.1    YES manual up                    up
	FastEthernet0/0.10     176.141.0.1     YES manual up                    up
	FastEthernet0/0.20     176.141.128.1   YES manual up                    up
	FastEthernet0/1        unassigned      YES unset  administratively down down
	Vlan1                  unassigned      YES unset  administratively down down
```

* `R0#show ip route`:
```
	     176.141.0.0/26 is subnetted, 3 subnets
	C       176.141.0.0 is directly connected, FastEthernet0/0.10
	C       176.141.64.0 is directly connected, FastEthernet0/0
	C       176.141.128.0 is directly connected, FastEthernet0/0.20
```

## task8 - check connections

### `net1` -> `net2` (`PC-64-3` -> `PC-0-3`)
* `ping 176.141.0.3`
```
	Reply from 176.141.0.3: bytes=32 time=0ms TTL=127
	Reply from 176.141.0.3: bytes=32 time=0ms TTL=127
	Reply from 176.141.0.3: bytes=32 time=0ms TTL=127
	Reply from 176.141.0.3: bytes=32 time=0ms TTL=127

	Ping statistics for 176.141.0.3:
	    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
	Approximate round trip times in milli-seconds:
	    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

### `net1` -> `net3` (`PC-64-3` -> `PC-128-3`)
* `ping 176.141.128.3`
```
	Reply from 176.141.128.3: bytes=32 time=0ms TTL=127
	Reply from 176.141.128.3: bytes=32 time=0ms TTL=127
	Reply from 176.141.128.3: bytes=32 time=0ms TTL=127
	Reply from 176.141.128.3: bytes=32 time=0ms TTL=127

	Ping statistics for 176.141.128.3:
	    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
	Approximate round trip times in milli-seconds:
	    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

### `net3` -> `net1` (`PC-128-4` -> `PC-64-6`)
* `ping 176.141.64.6`
```
	Reply from 176.141.64.6: bytes=32 time=0ms TTL=127
	Reply from 176.141.64.6: bytes=32 time=0ms TTL=127
	Reply from 176.141.64.6: bytes=32 time=0ms TTL=127
	Reply from 176.141.64.6: bytes=32 time=0ms TTL=127

	Ping statistics for 176.141.64.6:
	    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
	Approximate round trip times in milli-seconds:
	    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

and so on, all conections work fine!