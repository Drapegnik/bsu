/**
 * Created by Drapegnik on 4/25/17.
 */

import Product from './product.model';
import { checkIsFound, checkIdCast } from '../utils';

export const serializeProduct = product => ({
  id: product._id, // eslint-disable-line no-underscore-dangle
  title: product.title,
  type: product.type,
  price: product.price,
});

export const getAll = (req, res, next) => Product.find({})
  .then(products => products.map(serializeProduct))
  .then(products => res.status(200).json(products))
  .catch(err => next(err));

export const getById = (req, res, next) => {
  Promise.resolve(checkIdCast(req.params.id, Number))
    .then(id => Product.findById(id))
    .then(checkIsFound)
    .then(serializeProduct)
    .then(product => res.status(200).json(product))
    .catch(err => next(err));
};
