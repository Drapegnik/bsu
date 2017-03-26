/**
 * Created by Drapegnik on 26.03.17.
 */
/* eslint-disable no-console */

import * as db from './server/db';

Promise.resolve(db.connectDb())
  .then(mongoose => db.dropCollections(mongoose))
  .then((collections) => {
    console.log(`Mongoose: drop ${collections.length} collections: ${collections}`);
  })
  .then(() => db.initUsers())
  .then((users) => {
    console.log(`Mongoose: insert ${users.length} users:`);
    console.log(users);
  })
  .catch((err) => {
    console.log('Mongoose: error during init database');
    console.error(err);
  });
