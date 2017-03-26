/**
 * Created by Drapegnik on 26.03.17.
 */
/* eslint-disable no-console */

import * as db from './server/db';
import User from './server/api/user';

Promise.resolve(db.connect())
  .then(() => User.remove({}).exec())
  .then((result) => {
    console.log(`Mongoose: remove ${result.result.n} records from User`);
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
