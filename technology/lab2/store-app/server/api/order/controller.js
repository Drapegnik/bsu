/**
 * Created by Drapegnik on 4/25/17.
 */
import Order, { OrderItem } from './model';
import { serializeProduct } from '../product';

const serializeOrder = (order) => {
  const { client, summaryPrice, items } = order;
  const products = items.map(({ count, product }) => ({
    count,
    ...serializeProduct(product),
  }));
  return { client, summaryPrice, products };
};

export const getAll = (req, res, next) => Order.find({})
  .populate({
    path: 'items',
    populate: { path: 'product' },
  })
  .then(orders => orders.map(serializeOrder))
  .then(orders => res.status(200).json(orders))
  .catch(err => next(err));

export const create = (req, res, next) => {
  const { client, items, summaryPrice } = req.body;

  Promise.all(items.map(item => (new OrderItem(item)).save()))
    .then(orderItems => (
      new Order(
        { client, summaryPrice, items: orderItems.map(({ _id }) => _id) }).save()
    ))
    .then(({ _id }) => Order.findById(_id)
      .populate({
        path: 'items',
        populate: { path: 'product' },
      }))
    .then(order => res.status(200).json(serializeOrder(order)))
    .catch(err => next(err))
  ;
};
