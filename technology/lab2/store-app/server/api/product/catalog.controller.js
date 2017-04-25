/**
 * Created by Drapegnik on 4/25/17.
 */

import Catalog from './catalog.model';
import { serializeProduct } from './product.controller';
import { checkIsFound, checkIdCast } from '../utils';

const serializeCatalog = (catalog) => {
  const products = catalog.products.map(serializeProduct);
  return {
    id: catalog._id, // eslint-disable-line no-underscore-dangle
    name: catalog.name,
    isActive: catalog.isActive,
    products,
  };
};

export const getAll = (req, res, next) => Catalog.find({})
  .populate('products')
  .then(catalogs => catalogs.map(serializeCatalog))
  .then(catalogs => res.status(200).json(catalogs))
  .catch(err => next(err));

export const getById = (req, res, next) => {
  Promise.resolve(checkIdCast(req.params.id, Number))
    .then(id => Catalog.findById(id).populate('products'))
    .then(checkIsFound)
    .then(serializeCatalog)
    .then(catalog => res.status(200).json(catalog))
    .catch(err => next(err));
};

export const getActive = (req, res, next) => {
  Catalog.findOne({ isActive: true })
    .populate('products')
    .then(checkIsFound)
    .then(serializeCatalog)
    .then(catalog => res.status(200).json(catalog))
    .catch(err => next(err));
};

