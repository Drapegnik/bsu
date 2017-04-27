/**
 * Created by Drapegnik on 21.03.17.
 */

import { Router } from 'express';

import userRoutes from './user';
import productsRoutes from './product';
import ordersRoutes from './order';

const router = Router();

router.use('/products', productsRoutes);
router.use('/users', userRoutes);
router.use('/orders', ordersRoutes);

export default router;
