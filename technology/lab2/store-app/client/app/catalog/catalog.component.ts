/**
 * Created by Drapegnik on 5/16/17.
 */

import { Component } from '@angular/core';

import Catalog from '../_models/catalog';
import { ProductService } from '../_sevices/product.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html'
})
export class CatalogComponent {
  activeCatalog: Catalog;

  constructor(productService: ProductService) {
    productService.getActiveCatalog().subscribe(catalog => this.activeCatalog = catalog);
  }
}
