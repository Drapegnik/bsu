import Product from './product';

/**
 * Created by Drapegnik on 5/16/17.
 */

export default class Catalog {
  id: Number;
  isActive: boolean;
  products: Array<Product>;
  name: string;

  constructor({ id, isActive, name, products }) {
    this.id = id;
    this.isActive = isActive;
    this.products = products;
    this.name = name;
  }
}
