/**
 * Created by Drapegnik on 26.03.17.
 */

import mongoose from 'mongoose';
import crypto from 'crypto';

const Schema = mongoose.Schema;

/**
 * User mongoose Schema
 *  @config {Schema.String} _id
 *  @config {Schema.String} login
 *  @config {Schema.String} firstName
 *  @config {Schema.String} lastName
 *  @config {Schema.String} passwordHash
 *  @config {Schema.String} passwordSalt
 *  @config {Schema.String} role
 *  @config {Schema.Date} createdAt
 * @type {Schema}
 */
const UserSchema = new Schema({
  username: {
    type: String,
    unique: true,
    required: true,
  },
  passwordHash: String,
  passwordSalt: String,
  role: {
    type: String,
    enum: ['admin', 'order-manager', 'catalog-manager', 'transport-manager', 'product-manager'],
  },
  firstName: String,
  lastName: String,
  createdAt: { type: Date, default: new Date() },
});

UserSchema.virtual('password')
  .set(function set(password) {
    this.privatePassword = password;
    this.passwordSalt = this.makeSalt();
    this.passwordHash = this.encryptPassword(password);
  })
  .get(function get() { return this.privatePassword; });

UserSchema.methods = {
  /**
   * Authenticate - compare passwords
   *
   * @param {String} password - crypt password
   * @return {Boolean}
   * @api public
   */
  authenticate(password) { return this.encryptPassword(password) === this.passwordHash; },

  /**
   * Make salt
   *
   * @return {String}
   * @api public
   */
  makeSalt: () => crypto.randomBytes(16).toString('hex'),

  /**
   * Encrypt password
   *
   * @param {String} password
   * @return {String}
   * @api public
   */
  encryptPassword(password) {
    if (!password || !this.passwordSalt) {
      return '';
    }
    const salt = new Buffer(this.passwordSalt, 'hex');
    return crypto.pbkdf2Sync(password, salt, 10000, 64, 'sha1').toString('hex');
  },
};

const User = mongoose.model('User', UserSchema);
export default User;
