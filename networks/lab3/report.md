# lab3

* _Пажитных Иван Павлович_
* _3 курс, 1 группа, МСС_
* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab3)

## task 1

1. Для всех маршрутизаторов сети добавить описание интерфейсов (_description_)
2. Установить пароли на привилегированный режим доступа
3. Добавить заголовки (_MOTD banner_)
4. Присвоить имена коммутаторам сети
5. Проверить правильность

### 1. description

```
Router>enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface FastEthernet 0/0
Router(config-if)#description descFE
Router(config-if)#exit
```

### 2. password

```
Router(config)#enable secret abcd1234
```

* check login:

```
Router#disable
Router>enable
Password:
Router#
```

### 3. banner

```
Router(config)#banner motd # THIS IS BANNER! #
```

### 4. hostname

```
Router(config)#hostname MainRouter
MainRouter#
```

### 5. config

* `MainRouter#show running-config`:

```
Building configuration...

Current configuration : 737 bytes
!
version 12.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname MainRouter
!
enable secret 5 $1$mERr$cb.2iGZn12CECjdukdsKW.
!
spanning-tree mode pvst
!
interface FastEthernet0/0
 description descFE
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
!
interface Serial0/1/0
 description serial description 0/1/0
 no ip address
 clock rate 2000000
!
interface Serial0/1/1
 no ip address
 clock rate 2000000
!
interface Vlan1
 no ip address
 shutdown
!
ip classless
!
banner motd ^C THIS IS BANNER! ^C
!
line con 0
 password abcd1234
 login
line vty 0 4
 login
!
end
```

## task 2

### 1. schema

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1487602662/networks-2-1.png"/>

* check network connection from `PC0`:

  * `PC>ipconfig /all`

  ```
    Physical Address................: 0000.0CD3.A902
    IP Address......................: 172.17.10.21
    Subnet Mask.....................: 255.255.0.0
    Default Gateway.................: 172.17.10.1
    DNS Servers.....................: 0.0.0.0
  ```

  * `PC>ping 172.17.30.26`

  ```
    Pinging 172.17.30.26 with 32 bytes of data:
    Reply from 172.17.30.26: bytes=32 time=234ms TTL=128
    Reply from 172.17.30.26: bytes=32 time=109ms TTL=128
    Reply from 172.17.30.26: bytes=32 time=93ms TTL=128
    Reply from 172.17.30.26: bytes=32 time=125ms TTL=128

    Ping statistics for 172.17.30.26:
      Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
      Minimum = 93ms, Maximum = 234ms, Average = 140ms
  ```

* check network connection from `PC5`:

  * `PC>ipconfig /all`:

  ```
    Physical Address................: 0090.2104.3EE1
    IP Address......................: 172.17.30.26
    Subnet Mask.....................: 255.255.0.0
    Default Gateway.................: 172.17.30.1
    DNS Servers.....................: 0.0.0.0
  ```

  * `PC>ping 172.17.10.21`:

  ```
    Pinging 172.17.10.21 with 32 bytes of data:
    Reply from 172.17.10.21: bytes=32 time=124ms TTL=128
    Reply from 172.17.10.21: bytes=32 time=125ms TTL=128
    Reply from 172.17.10.21: bytes=32 time=109ms TTL=128
    Reply from 172.17.10.21: bytes=32 time=125ms TTL=128

    Ping statistics for 172.17.10.21:
      Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
      Minimum = 109ms, Maximum = 125ms, Average = 120ms
  ```

### 2. Создать VLANs на коммутаторе `S0`

```
Switch>
Switch>enable
Switch#config t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#hostname S0
S0(config)#vlan 10
S0(config-vlan)#name Faculty/Staff
S0(config-vlan)#vlan 20
S0(config-vlan)#name Students
S0(config-vlan)#vlan 30
S0(config-vlan)#name Guest(Default)
S0(config-vlan)#vlan 99
S0(config-vlan)#name Management&Native
S0(config-vlan)#exit
S0(config)#exit
```

* on `S1` and `S2` the same way

### 3. Проверить конфигурацию `VLANs` на всех коммутаторах

* `S0#show vlan brief`: (for `S1` and `S2` the same)

```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
10   Faculty/Staff                    active
20   Students                         active
30   Guest(Default)                   active
99   Management&Native                active
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

### 4. Назначить `VLANs` на порты

```
S1(config)#interface fastEthernet 0/3
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 10
S1(config-if)#interface fastEthernet 0/2
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 20
S1(config-if)#interface fastEthernet 0/1
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 30
```

* Аналогичная настройка для `S2`
* Пакеты не доходят, т.к. `VLANs` не настроены на портах `S0`

### 5. Конфигурирование `trunk` портов

* for `S0`:

```
  S0(config)#interface fastEthernet 0/1
  S0(config-if)#switchport mode trunk
  S0(config-if)#
      %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down
      %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to up
  S0(config-if)#switchport trunk native vlan 99
  S0(config-if)#interface fastEthernet 0/2
  S0(config-if)#switchport mode trunk
  S0(config-if)#
      %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/2, changed state to down
      %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/2, changed state to up
  S0(config-if)#exit
  S0(config)#exit
```

* for `S1` and `S2`:

```
  S2(config)#interface fastEthernet 0/4
  S2(config-if)#switchport mode trunk
  S2(config-if)#
      %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/4, changed state to down
      %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/4, changed state to up
  S2(config-if)#switchport trunk native vlan 99
  S2(config-if)#
      %SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking FastEthernet0/4 on VLAN0099. Port consistency restored.
      %SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking FastEthernet0/4 on VLAN0001. Port consistency restored.
  S2(config-if)#exit
  S2(config)#exit
```

### 6. Протестировать сеть

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1487602662/networks-2-2.png"/>

* `S1>show vlan brief`:

```
  10   Faculty/Staff                    active    Fa0/3
  20   Students                         active    Fa0/2
  30   Guest(Default)                   active    Fa0/1
  99   Management&Native                active
```
