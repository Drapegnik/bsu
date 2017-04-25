/**
 * Created by Drapegnik on 4/25/17.
 */

import { Order, OrderItem } from '../api/order';

export function initOrdersItems(products) {
  // eslint-disable-next-line no-underscore-dangle
  const cheapProducts = products.filter(p => p.price < 1000).map(p => p._id);

  const ordersItemsPromises = cheapProducts.map((product, index) =>
    (new OrderItem({
      product,
      count: (index + 1) * 10,
    })).save());

  return Promise.all(ordersItemsPromises);
}

export function initOrder(orderItemsWithProducts) {
  const client = {
    name: 'Test Client',
    email: 'client@test.com',
  };
  const items = [];
  let summaryPrice = 0;

  orderItemsWithProducts.forEach((orderItem) => {
    items.push(orderItem._id); // eslint-disable-line no-underscore-dangle
    summaryPrice += orderItem.price;
  });

  return (new Order({ client, items, summaryPrice })).save();
}
