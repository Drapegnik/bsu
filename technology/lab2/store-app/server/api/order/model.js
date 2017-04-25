/**
 * Created by Drapegnik on 4/25/17.
 */

import mongoose, { Schema } from 'mongoose';

/**
 * OrderItem mongoose Schema - Product and count mapper
 *  @config {Schema.ObjectId} _id
 *  @config {Schema.Number} product
 *  @config {Schema.Number} count
 */
const OrderItemSchema = new Schema({
  product: {
    type: Number,
    ref: 'Product',
    required: true,
  },
  count: {
    type: Number,
    required: true,
  },
});

// Model should be populated with Product first
OrderItemSchema.virtual('price')
  .get(function () { // eslint-disable-line func-names
    if (!this.product.price) {
      throw (new Error('Model should be populated with Product first'));
    }

    return this.product.price * this.count;
  });

/**
 * Order mongoose Schema
 *  @config {Schema.ObjectId} _id
 *  @config {Schema.Object} client
 *  @config {Schema.String} client.name
 *  @config {Schema.String} client.email
 *  @config {Schema.Number} summaryPrice
 *  @config {Schema.Array} items
 * @type {Schema}
 */
const OrderSchema = new Schema({
  client: {
    name: { type: String, required: true },
    email: { type: String, required: true },
  },
  summaryPrice: {
    type: Number,
    required: true,
  },
  items: [{
    type: Schema.ObjectId,
    ref: 'OrderItem',
    required: true,
  }],
});

export const OrderItem = mongoose.model('OrderItem', OrderItemSchema);
const Order = mongoose.model('Order', OrderSchema);
export default Order;
