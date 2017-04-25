/**
 * Created by Drapegnik on 21.03.17.
 */

import { Router } from 'express';

import userRoutes from './user';
import productsRoutes from './product';

const router = Router();

router.use('/products', productsRoutes);
router.use('/users', userRoutes);

export default router;
