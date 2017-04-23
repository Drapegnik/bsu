/**
 * Created by Drapegnik on 26.03.17.
 */

import { User } from '../api/user';

export default function (username, password, done) {
  User.findOne({ username }, (err, user) => {
    if (err) { return done(err); }

    if (!user) {
      return done(null, false, { username: 'Incorrect username' });
    }

    if (!user.authenticate(password)) {
      return done(null, false, { password: 'Incorrect password' });
    }

    return done(null, user);
  });
}
