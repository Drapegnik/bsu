/**
 * Created by Drapegnik on 23.04.17.
 */

import { Product } from '../api/catalog';
import data from './products.json';

export default function initProducts() {
  const productsPromises = [];

  data.forEach((productData) => {
    productsPromises.push((new Product(productData)).save());
  });

  return Promise.all(productsPromises);
}
