# Лабораторная работа 1
«*RMI*-технология»

## demo
[documentation](https://drapegnik.github.io/bsu/programming/java/sem6/lab1/docs/index.html)

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1489673732/javasem6lab1.png" width="700px"/>

## task1 Проектирование приложений на базе *RMI*
* Информация хранится в базе данных. 
* Реализовать несколько методов изменения содержимого базы данных. 
* Задача демонстрируется на нескольких машинах. 
* База данных должна содержать несколько таблиц.
* Создать приложение с интерфейсом пользователя (на базе **JFC Swing**) 

```
Имеется информация об итогах сессии. 
Сведения о каждом студенте — это фамилия, номер группы и результаты экзаменов. 
Показать студентов, не сдавших сессию, предложить их к исключению и, если потребуется, исключить.
```

## task2 Создание документации
* Создать для своей первой задачи документацию.
* Использовать **javadoc**
* Должна быть информация об авторе. 
* Показать полное описание метода (параметры, исключения, результат). 
* Использовать ссылки (`@link`), *HTML*. 
* Должны работать ссылки на стандартную документацию.

## task3 Использование технологий разбора *XML*
* Для `task1` данные хранятся в *xml*-файле, а не в базе данных. 
* Интерфейс *RMI* и интерфейс пользователя должен остаться таким же
* Также должна быть возможность проверки *xml*-файла на корректность. 
* С некорректными данными запретить возможность работы. 
* Разбор осуществляется посредством технологии *StAX*.

***
## Setup
* set `RMI_PORT` and `RMI_HOST` environment variables
* create out dir (default `out/production/lab1`)

## Build
* `bash build.sh` for build all classes from `src/`
* `bash build_doc.sh` for generate documentation

## Run
* start *RMI* `bash run_rmi.sh {out_dir}`
* start *Server* `bash run_server.sh {db_type} {port} {host} {out_dir}`
* start *Client* `bash run_client.sh {port} {host} {out_dir}`

## Note
* for running on remote machines you need to create `server.policy`, `client.policy` files and put it in `src/`
