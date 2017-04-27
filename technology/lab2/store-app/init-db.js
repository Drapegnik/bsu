/**
 * Created by Drapegnik on 26.03.17.
 */
/* eslint-disable no-console */

import * as db from './server/db';
import { Catalog, Product } from './server/api/product';
import { Order, OrderItem } from './server/api/order';
import { User } from './server/api/user';

Promise.resolve(db.connectDb())
  .then(mongoose => db.dropCollections(mongoose))
  .then((collections) => {
    console.log(`Mongoose: drop ${collections.length} collections: ${collections}`);
    return db.initUsers();
  })
  .then(() => User.find({}))
  .then((users) => {
    console.log(`Mongoose: insert ${users.length} users`);
    // console.log(users);
    return db.initProducts();
  })
  .then(() => Product.find({}))
  .then((products) => {
    console.log(`Mongoose: insert ${products.length} products`);
    // console.log(products);
    return db.initCatalogs(products);
  })
  .then(() => Catalog.find({}))
  .then((catalogs) => {
    console.log(`Mongoose: insert ${catalogs.length} catalogs`);
    // console.log(catalogs);
  })
  .then(() => Product.find({}))
  .then(db.initOrdersItems)
  .then(() => OrderItem.find({}).populate('product'))
  .then((orderItemsWithProducts) => {
    console.log(`Mongoose: insert ${orderItemsWithProducts.length} order items`);
    // console.log(orderItemsWithProducts);
    return orderItemsWithProducts;
  })
  .then(db.initOrder)
  .then(() => Order.find({}))
  .then((orders) => {
    console.log(`Mongoose: insert ${orders.length} orders`);
    // console.log(orders);
  })
  .then(() => process.exit())
  .catch((err) => {
    console.log('Mongoose: error during init database');
    console.error(err);
    process.exit();
  });
