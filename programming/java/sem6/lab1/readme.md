# Лабораторная работа 1
«*RMI*-технология»

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

***
## Setup
* set `RMI_PORT` and `RMI_HOST` environment variables
* create out dir (default `out/production/lab1`)

## Run
* compile all classes from `src/` in out dir (default is `out/production/lab1`)
* run `dbDriver.main()` for creating database
* run `run_rmi.sh` for start rmi (you can specify out dir or use default)
* start `Server` (`java path/to/outdir/Server`)
* after message `Server ready` start `Client` (`java path/to/outdir/Client`)

