/**
 * Created by Drapegnik on 4/25/17.
 */
import mongoose from 'mongoose';

import User from './model';
import { checkIsFound, checkIdCast } from '../utils';

const serializeUser = user => ({
  id: user._id, // eslint-disable-line no-underscore-dangle
  username: user.username,
  firstName: user.firstName,
  lastName: user.lastName,
  role: user.role,
});

export const getAll = (req, res, next) => User.find({})
  .then(users => users.map(serializeUser))
  .then(users => res.status(200).json(users))
  .catch(err => next(err));

export const getById = (req, res, next) => {
  Promise.resolve(checkIdCast(req.params.id, mongoose.Types.ObjectId))
    .then(id => User.findById(id))
    .then(checkIsFound)
    .then(serializeUser)
    .then(user => res.status(200).json(user))
    .catch(err => next(err));
};
