/**
 * Created by Drapegnik on 5/16/17.
 */

import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import Catalog from '../_models/catalog';
import Product from '../_models/product';
import { ProductsService } from '../_sevices/products.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html'
})
export class CatalogComponent {
  public static selectedProducts: Array<Product>;
  activeCatalog: Catalog;
  isCreateMode: boolean;
  title: string;

  constructor(productsService: ProductsService, route: ActivatedRoute) {
    this.isCreateMode = route.snapshot.data['isCreateMode'];
    productsService.getActiveCatalog().subscribe((catalog) => {
      this.activeCatalog = catalog;
      this.title = `Catalog «${this.activeCatalog.name}»`;
      if (this.isCreateMode) {
        this.title += '/ choose products for order';
      }
    });
  }

  public canNext = () => !this.activeCatalog.products.filter(p => p.selected).length;

  public handleNext = () => {
    console.log(this.activeCatalog.products);
    CatalogComponent.selectedProducts = this.activeCatalog.products.filter(p => p.selected);
  }
}
