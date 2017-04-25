/**
 * Created by Drapegnik on 23.04.17.
 */

import { Router } from 'express';

import Product from './product.model';
import Catalog from './catalog.model';
import * as productController from './product.controller';
import * as catalogController from './catalog.controller';

const router = Router();

// order is important!
router.get('/catalogs', catalogController.getAll); // catalogs routes first
router.get('/catalogs/active', catalogController.getActive);
router.get('/catalogs/:id', catalogController.getById);

router.get('/', productController.getAll);
router.get('/:id', productController.getById);

export { Product, Catalog };
export default router;
