/**
 * Created by Drapegnik on 5/16/17.
 */

import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import Catalog from '../_models/catalog';
import Product from '../_models/product';
import { ProductService } from '../_sevices/product.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html'
})
export class CatalogComponent {
  public static selectedProducts: Array<Product>;
  activeCatalog: Catalog;
  isCreateMode: boolean;

  constructor(productService: ProductService, route: ActivatedRoute) {
    productService.getActiveCatalog().subscribe(catalog => this.activeCatalog = catalog);
    this.isCreateMode = route.snapshot.data['isCreateMode'];
  }

  public canNext = () => !this.activeCatalog.products.filter(p => p.selected).length;

  public setAll = (value) => this.activeCatalog.products.forEach(p => p.selected = value);

  public handleNext = () => {
    CatalogComponent.selectedProducts = this.activeCatalog.products.filter(p => p.selected);
    this.setAll(false);
  }
}
