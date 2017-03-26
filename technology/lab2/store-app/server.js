/**
 * Created by Drapegnik on 21.03.17.
 */

import express from 'express';
import path from 'path';
import fs from 'fs';
import logger from 'morgan';
import bodyParser from 'body-parser';
import cors from 'cors';
import { createServer } from 'http';

import api from './server/api';
import config from './server/config';
import { connect } from './server/db';


const client = JSON.parse(fs.readFileSync('.angular-cli.json', 'utf8'));
const publicPath = path.join(__dirname, client.apps[0].outDir);
const app = express();
connect();

app.use(cors());
app.use(logger('dev'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(publicPath));

app.use('/api', api);

app.use((req, res, next) => {
  const err = new Error('Not Found');
  err.status = 404;
  next(err);
});

app.use((err, req, res, next) => { // eslint-disable-line no-unused-vars
  console.error(err.message); // eslint-disable-line no-console
  res.status(err.status || 500);
  res.send(err.message);
});

app.get('*', (req, res) => {
  res.sendFile(path.join(publicPath, 'index.html'));
});

createServer(app).listen(config.port, () => {
  console.log('Server running at http://localhost:3000'); // eslint-disable-line no-console
});
