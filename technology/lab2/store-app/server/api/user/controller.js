/**
 * Created by Drapegnik on 4/25/17.
 */
import mongoose from 'mongoose';

import User from './model';
import { checkIsFound, checkIdCast } from '../utils';

const serializeUser = ({ _id, username, firstName, lastName, role }) =>
  ({ id: _id, username, firstName, lastName, role });

export const getAll = (req, res, next) => User.find({})
  .then(users => users.map(serializeUser))
  .then(users => res.status(200).json(users))
  .catch(err => next(err));

// eslint-disable-next-line no-unused-vars
export const getMe = (req, res, next) => res.status(200).json(serializeUser(req.user));

export const getById = (req, res, next) => {
  Promise.resolve(checkIdCast(req.params.id, mongoose.Types.ObjectId))
    .then(id => User.findById(id))
    .then(checkIsFound)
    .then(serializeUser)
    .then(user => res.status(200).json(user))
    .catch(err => next(err));
};
