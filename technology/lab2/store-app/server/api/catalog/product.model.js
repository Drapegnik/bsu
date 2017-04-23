/**
 * Created by Drapegnik on 23.04.17.
 */

import mongoose, { Schema } from 'mongoose';

/**
 * Product mongoose Schema
 *  @config {Schema.Number} _id
 *  @config {Schema.String} title
 *  @config {Schema.String} type
 *  @config {Schema.Number} price
 * @type {Schema}
 */
const ProductSchema = new Schema({
  _id: {
    type: Number,
    unique: true,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    enum: ['phone', 'laptop', 'other'],
    default: 'other',
  },
  price: {
    type: Number,
    required: true,
  },
});

const Product = mongoose.model('Product', ProductSchema);
export default Product;
