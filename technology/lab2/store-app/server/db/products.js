/**
 * Created by Drapegnik on 23.04.17.
 */

import { Product, Catalog } from '../api/product';
import data from './products.json';

export const initProducts = () => Promise.all(
  data.map(productData => (new Product({ ...productData, _id: productData.id })).save())
);

export const initCatalogs = (products) => {
  const phones = products.filter(p => p.type === 'phone').map(p => p._id); // eslint-disable-line no-underscore-dangle
  const laptops = products.filter(p => p.type === 'laptop').map(p => p._id); // eslint-disable-line no-underscore-dangle
  const catalogs = [
    { _id: 1, name: 'Phones', products: phones, isActive: true },
    { _id: 2, name: 'Laptops', products: laptops },
  ];
  return Promise.all(catalogs.map(catalogData => (new Catalog(catalogData)).save()));
};
