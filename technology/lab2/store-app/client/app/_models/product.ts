/**
 * Created by Drapegnik on 5/15/17.
 */

export default class Product {
  id: number;
  title: string;
  count: number;
  type: string;
  price: number;

  constructor({ id, title, count, type, price }) {
    this.id = id;
    this.title = title;
    this.count = count;
    this.type = type;
    this.price = price;
  }
}
