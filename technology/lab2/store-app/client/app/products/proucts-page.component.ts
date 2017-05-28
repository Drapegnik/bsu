/**
 * Created by Drapegnik on 5/29/17.
 */

import { Component } from '@angular/core';

import Product from '../_models/product';
import { ProductsService } from '../_sevices/products.service';


@Component({
  selector: 'app-orders-page',
  template: `
    <app-products-table [products]="products"></app-products-table>
  `
})
export class ProductsPageComponent {
  products: Array<Product>;

  constructor(private productsService: ProductsService) {
    productsService.getAll().subscribe(products => this.products = products);
  }
}
