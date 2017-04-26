/**
 * Created by Drapegnik on 26.03.17.
 */

import { Router } from 'express';

import User from './model';
import * as controller from './controller';

const router = Router();
router.get('/', controller.getAll);
router.get('/me', controller.getMe);
router.get('/:id', controller.getById);

export { User }; // eslint-disable-line import/prefer-default-export
export default router;
