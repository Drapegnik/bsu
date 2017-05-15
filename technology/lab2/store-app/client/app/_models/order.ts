import Product from './product';
/**
 * Created by Drapegnik on 5/15/17.
 */

class Client {
  email: string;
  name: string;


  constructor(email: string, name: string) {
    this.email = email;
    this.name = name;
  }
}

export default class Order {
  client: Client;
  summaryPrice: number;
  products: Array<Product>;

  constructor({ client: { email, name }, summaryPrice, products }) {
    this.client = new Client(email, name);
    this.summaryPrice = summaryPrice;
    this.products = products;
  }
}
