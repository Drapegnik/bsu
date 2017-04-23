/**
 * Created by Drapegnik on 23.04.17.
 */

import mongoose, { Schema } from 'mongoose';

/**
 * Catalog mongoose Schema
 *  @config {Schema.Number} _id
 *  @config {Schema.String} name
 * @type {Schema}
 */
const CatalogSchema = new Schema({
  _id: {
    type: Number,
    unique: true,
    required: true,
  },
  name: {
    type: String,
    unique: true,
    required: true,
  },
  products: [{ type: Number, ref: 'Product' }],
});

const Catalog = mongoose.model('Catalog', CatalogSchema);
export default Catalog;
