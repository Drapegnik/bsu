# Лабораторная работа 2
Создание приложения на основе *Use Case*

## [store-app](https://github.com/Drapegnik/bsu/blob/master/technology/lab2/store-app)
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1490542775/mean1.png)

* [MongoDB](https://www.mongodb.com/)
* [Express](http://expressjs.com/)
* [Angular 2](https://angular.io/) + [TypeScript](https://www.typescriptlang.org/)
* [Node.js](https://nodejs.org/en/)

## use case diagram
I use [Enterprise Architect](http://www.sparxsystems.com/products/ea). Model saved in [`lab2.eap`](https://github.com/Drapegnik/bsu/blob/master/technology/lab2/lab2.eap)
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1490050601/tp-2-1.png)

## task
Смоделировать  и реализовать систему обработки заказов.

### Спецификация системы.

* Компания – торговый посредник, продающая товары различных производителей (заказчик системы).
* Дважды в год компания публикует каталог продуктов, который рассылается клиентам и другим заинтересованным лицам.
* Клиенты приобретают товары, направляя в компанию перечень продуктов с информацией об оплате. Компания выполняет заказы и отправляет товары по адресам клиентов.
* Система должна отслеживать заказ от момента его получения до отправки товара.
* Клиенты могут возвращать товары, оплачивая, возможно, некоторые издержки.
* Компания пользуется услугами различных транспортных компаний.


### Замечание
Интерфейс пользователя разработать и реализовать полностью для всей системы.