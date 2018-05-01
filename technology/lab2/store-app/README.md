# store-app

[Angular2](https://angular.io)/[Node.js](https://nodejs.org/en/) webapp.

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1490542775/mean2.jpg)

**TL;DR:**

```bash
npm i
npm start
```

## development server

Run `npm run client` for a dev server. Navigate to http://localhost:4200/. The
app will automatically reload if you change any of the source files.

:warning: **Warning**: Cookies doesn't works in this mode, because browser doesn't attach cookie for different domains (e.g. `localhost:3000` & `localhost:4200`). With builded client in case `npm run server` everything should works.

> You can try to solve issue with cookies by enabling proxying on client in dev mode

## code scaffolding

Run `ng generate component component-name` to generate a new component. You can
also use `ng generate directive/pipe/service/class/module`.

## code style

Run `npm lint` to check client and server code style.

## build

Run `npm run build` to build the client. The build artifacts will be stored in
the `dist/` directory.

## server

Run `npm run server` for build client and start server. Open
http://localhost:3000/.

## init

Run `npm run init-db` for inserting init data into database

> see the [`docs`](http://drapegnik.github.io/bsu/technology/lab2/docs)

## demo

### login

<p align="center">
<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1496078049/store-app-login.png" width="700px"/>
</p>

### orders list

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1496078050/store-app-orders.png)

### create order

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1496078051/store-app-create-order1.png)

<p align="center">
<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1496078050/store-app-create-order2.png" width="700px"/>
</p>

### edit catalog

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1496078050/store-app-edit-catalog.png)

### products table

![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1496078050/store-app-products.png)

> P.S: you can easy change app theme by replacing theme name from [`bootswatch`](https://bootswatch.com/) [here](https://github.com/Drapegnik/bsu/blob/master/technology/lab2/store-app/client/styles.css#L2)
