/**
 * Created by Drapegnik on 26.03.17.
 */

import passport from 'passport';
import { Strategy as LocalStrategy } from 'passport-local';

import { User } from '../api/user';

passport.use(new LocalStrategy({
  usernameField: 'username',
  passwordField: 'password',
}, (username, password, done) => {
  User.findOne({ username }, (err, user) => {
    if (err) {
      return done(err);
    }

    if (!user) {
      return done(null, false, { username: 'Incorrect username' });
    }

    if (!user.authenticate(password)) {
      return done(null, false, { password: 'Incorrect password' });
    }

    return done(null, user);
  });
}));

passport.serializeUser((user, done) => done(null, user.id));

passport.deserializeUser((id, done) => User.findById(id, (err, user) => {
  if (err) {
    done(err);
  }
  done(null, user);
}));

export default passport;
