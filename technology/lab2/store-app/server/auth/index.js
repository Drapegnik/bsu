/**
 * Created by Drapegnik on 26.03.17.
 */

import { Router } from 'express';

import passport from './passport';

const router = Router();

/**
 * Route for username post request
 */
router.post('/login',
  passport.authenticate('local', { failureMessage: true }),

  (req, res, next) => { // eslint-disable-line no-unused-vars
    if (req.user) {
      res.sendStatus(200);
    }

    res.status(200);
  });

/**
 * Log out route
 */
router.get('/logout', (req, res, next) => { // eslint-disable-line no-unused-vars
  req.logout();
  res.redirect('/');
});

export default router;
export { passport };
