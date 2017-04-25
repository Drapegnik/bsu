/**
 * Created by Drapegnik on 4/24/17.
 */

export default class User {
  username: string;
  firstName: string;
  lastName: string;
  role: string;
  isAnonymous: boolean;

  constructor({ username = 'anon', firstName = '', lastName = '', role = '', isAnonymous = false }) {
    this.isAnonymous = isAnonymous;
    this.username = username;
    this.firstName = firstName;
    this.lastName = lastName;
    this.role = role;
  }
}
