/**
 * Created by Drapegnik on 26.03.17.
 */

import { User } from '../api/user';
import data from './users.json';

export default function initUsers() {
  const userPromises = [];
  data.forEach(userData => userPromises.push((new User(userData)).save()));
  return Promise.all(userPromises);
}
