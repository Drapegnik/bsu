/**
 * Created by Drapegnik on 23.04.17.
 */

import { Product, Catalog } from '../api/catalog';
import data from './products.json';

export function initProducts() {
  const productsPromises = [];
  data.forEach(productData => productsPromises.push((
    new Product({
      ...productData,
      _id: productData.id,
    })).save()));
  return Promise.all(productsPromises);
}

export function initCatalogs(products) {
  const catalogsPromises = [];
  const phones = products.filter(p => p.type === 'phone').map(p => p._id);
  const laptops = products.filter(p => p.type === 'laptop').map(p => p._id);
  const catalogs = [
    { _id: 1, name: 'Phones', products: phones },
    { _id: 2, name: 'Laptops', products: laptops },
  ];
  catalogs.forEach(catalogData => catalogsPromises.push((new Catalog(catalogData)).save()));
  return Promise.all(catalogsPromises);
}
