/**
 * Created by Drapegnik on 5/29/17.
 */

import { Component, Input } from '@angular/core';

import Product from '../_models/product';

@Component({
  selector: 'app-products-table',
  templateUrl: './products-table.component.html'
})
export class ProductsTableComponent {
  @Input() products: Array<Product>;
  @Input() selectable: boolean;
  @Input() title: string;

  public setAll = (value) => this.products.forEach(p => p.selected = value);
}
