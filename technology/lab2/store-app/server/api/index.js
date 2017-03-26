/**
 * Created by Drapegnik on 21.03.17.
 */

import { Router } from 'express';

const router = Router();

router.get('/', (req, res, next) => { // eslint-disable-line no-unused-vars
  res.send('Hello from api!');
});

export default router;

