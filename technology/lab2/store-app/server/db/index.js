/**
 * Created by Drapegnik on 26.03.17.
 */

import connectDb from './mongoose';
import { User } from '../api/user';
import { initProducts, initCatalogs } from './products';
import { initOrder, initOrdersItems } from './orders';

import usersData from './users.json';

export const initUsers = () => Promise.all(usersData.map(user => (new User(user)).save()));

export const dropCollections = (mongoose) => {
  const collections = Object.keys(mongoose.connection.collections);

  const promises = collections.map(
    name =>
      new Promise((resolve, reject) => {
        const collection = mongoose.connection.collections[name];

        collection.drop((err) => {
          if (err && err.message !== 'ns not found') {
            reject(err);
          }

          resolve(name);
        });
      }));

  return Promise.all(promises);
};

export { connectDb, initProducts, initCatalogs, initOrder, initOrdersItems };
