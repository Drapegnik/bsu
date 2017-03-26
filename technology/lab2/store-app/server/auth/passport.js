/**
 * Created by Drapegnik on 26.03.17.
 */

import passport from 'passport';
import { Strategy as LocalStrategy } from 'passport-local';

import { User } from '../api/user';
import checkAuth from './checkAuth';

passport.use(new LocalStrategy({
  usernameField: 'username',
  passwordField: 'password',
}, checkAuth));

passport.serializeUser((user, done) => done(null, user.id));

passport.deserializeUser((id, done) => User.findById(id, (err, user) => {
  if (err) {
    done(err);
  }
  done(null, user);
}));

export default passport;
