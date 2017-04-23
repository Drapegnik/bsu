/**
 * Created by Drapegnik on 23.04.17.
 */

import mongoose from 'mongoose';

const Schema = mongoose.Schema;

/**
 * Product mongoose Schema
 *  @config {Schema.String} _id
 *  @config {Schema.Number} id
 *  @config {Schema.String} title
 *  @config {Schema.String} type
 *  @config {Schema.Number} price
 * @type {Schema}
 */
const ProductSchema = new Schema({
  id: {
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
