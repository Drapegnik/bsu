# Лабораторная работа 3

«Проектирование сетевых приложений»

## task

* Проектирование сетевых приложений с использованием сетевых классов,
  проектирование интерфейса пользователя средствами библиотек **JFC Swing**,
  использование компоновок.
* Создать оконное приложение для решения следующего задания.
* Реализовать схему _«сервер – много клиентов»_. Передача всегда идет через
  сервер! При передаче файлов передавать не по одному байту.

## problem

> Поиск в удаленной папке больших файлов и их передача.

## demo

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1504365635/java-sem5lab3.png)

#### server log

```
Server start at MBP-Ivan/192.168.0.187 and listen 8000 port
New connection -> (Client#1)
GET /Users/Drapegnik/projects/bsu/programming/java/sem5/lab3/small.txt -> (Client#1)
Start sending file -> (Client#1)
File send! -> (Client#1)
```

#### client log

```
Client#1: successfully connect to MBP-Ivan/192.168.0.187:8000
Client#1: GET /Users/Drapegnik/projects/bsu/programming/java/sem5/lab3/small.txt 200
Client#1: receive 'line1'
Client#1: receive 'line2'
Client#1: receive 'line3'
Client#1: receive 'line4'
Client#1: receive 'line5'
Client#1: receive 'line6'
```
