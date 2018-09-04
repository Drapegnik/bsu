# Лабораторная работа 2

«Сервлеты»

## demo

### step 1 - App name

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1493688911/java-gen-step1.png" width="700px">

### step 2 - Front-end

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1493688911/java-gen-step2.png" width="700px">

### step 3 - Styles

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1493688911/java-gen-step3.png" width="700px">

### step 4 - Back-end

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1493688911/java-gen-step4.png" width="700px">

### step 5 - Results

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1493688911/java-gen-step5.png" width="700px">

### step 5 - Empty results

<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1493688911/java-gen-step6.png" width="700px">

## task1 Изучение сервлетов, использование механизма сессий

- Создать мастер создания чего-либо, в котором пользователи двигаются через
  цепочку шагов.
- Информация каждого шага запоминается в атрибутах сессии.
- Можно двигаться вперед и назад, обязательно восстанавливая соответствующие
  значения шага.
- Задание подразумевает наличие красочного и отличного от коллег интерфейса.

> [Примеры шаблонов](http://office.microsoft.com/ru-ru/templates/FX102832616.aspx)

## task2 Использование _JSP_, разработка собственных тегов

- Разработать собственный тег.
- Некоторые параметры задавать атрибутом, некоторые – в теле тега.
- В случае некорректных данных (предусмотреть хотя бы один вариант)) переходить
  на специальную страницу обработки ошибок (атрибут `errorPage`, `isErrorPage`).
- Некую красивую шапку оформить в отдельном `jsp`-файле и вставить в основной
  (`jsp:include` или т.п.).

---

## Dependencies

- [`tomcat server`](http://tomcat.apache.org/download-80.cgi)
- [`jstl`](https://tomcat.apache.org/taglibs/standard/)

## Notes

> you should add `javax.servlet.jsp.jstl.jsp` and
> `javax.servlet.jsp.jstl-api.jar`in
> [`WEB-INF/lib`](https://github.com/Drapegnik/bsu/tree/master/programming/java/sem6/lab2/web/WEB-INF/lib)
> directory
