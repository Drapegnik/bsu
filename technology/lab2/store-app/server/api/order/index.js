/**
 * Created by Drapegnik on 4/25/17.
 */

import { Router } from 'express';

import Order, { OrderItem } from './model';
import * as controller from './controller';

const router = Router();
router.get('/', controller.getAll);
router.post('/', controller.create);

export { Order, OrderItem };
export default router;
