/**
 * Created by Drapegnik on 26.03.17.
 */
/* eslint-disable no-console */

import mongoose from 'mongoose';

import config from '../config';

function connect() {
  mongoose.connect(config.mongoose.url, config.mongoose.options);

  mongoose.connection.on('connected', () => {
    console.log(`Mongoose: connected to ${config.mongoose.url}`);
  });

  mongoose.connection.on('error', (err) => {
    console.log(`Mongoose: connection error: ${err}`);
  });

  mongoose.connection.on('disconnected', () => {
    console.log('Mongoose: connection disconnected');
  });
}

export { mongoose, connect };
