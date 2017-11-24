# Лабораторная работа 4

«Синхронизация потоков»

## Условие

> Реализовать _CarPark controller_ программу, которая следит за состоянием
> гаража и разъешает въезд машин, только если в гараже есть свободные места.

* Моделирование операций прибытия и выезда из гаража, объем гаража равен `k`
* Реализовать операции.
* Написать демонстрационную программу.
* Использовать многопоточность и синхранизацию

## Выполнение

```
(garage): status: [0/3] taked!
(main): There are 3 places and 5 cars.
(main): Start race! Type any key terminating:
--------------------------------------
(car#1): ENTER
(garage): status: [1/3] taked!
--------------------------------------
(car#3): ENTER
(garage): status: [2/3] taked!
--------------------------------------
(car#2): ENTER
(garage): status: [3/3] taked!
--------------------------------------
(car#1): LEAVE
(garage): status: [2/3] taked!
--------------------------------------
(car#4): ENTER
(garage): status: [3/3] taked!
--------------------------------------
(car#3): LEAVE
(garage): status: [2/3] taked!
--------------------------------------
(car#2): LEAVE
(garage): status: [1/3] taked!
--------------------------------------
q
q
(car#0): ENTER
(garage): status: [2/3] taked!
--------------------------------------
(car#1): ENTER
(garage): status: [3/3] taked!
--------------------------------------
(car#4): LEAVE
(garage): status: [2/3] taked!
--------------------------------------
(car#0): LEAVE
(garage): status: [1/3] taked!
(car#0): enters - 1, leaves - 1
--------------------------------------
(car#4): enters - 1, leaves - 1
--------------------------------------
(car#1): LEAVE
(garage): status: [0/3] taked!
(car#1): enters - 2, leaves - 2
--------------------------------------
(car#3): ENTER
(garage): status: [1/3] taked!
--------------------------------------
(car#2): ENTER
(garage): status: [2/3] taked!
--------------------------------------
(car#3): LEAVE
(garage): status: [1/3] taked!
(car#3): enters - 2, leaves - 2
--------------------------------------
(car#2): LEAVE
(garage): status: [0/3] taked!
(car#2): enters - 2, leaves - 2
--------------------------------------
(main): All child threads terminate successfully!
(garage): status: [0/3] taked!
```
