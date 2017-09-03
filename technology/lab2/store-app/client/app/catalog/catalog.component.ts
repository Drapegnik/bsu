/**
 * Created by Drapegnik on 5/16/17.
 */

import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import User from '../_models/user';
import Catalog from '../_models/catalog';
import Product from '../_models/product';
import { ProductsService } from '../_sevices/products.service';
import { CatalogGuard } from '../_guards/catalog.guard';
import { AuthenticationService } from "../_sevices/authentication.service";


@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html'
})
export class CatalogComponent {
  public static selectedProducts: Array<Product>;
  activeCatalog: Catalog;
  isCreateMode: boolean;
  title: string;
  user: User;

  constructor(private productsService: ProductsService,
              private route: ActivatedRoute,
              private authService: AuthenticationService) {
    this.isCreateMode = route.snapshot.data['isCreateMode'];

    authService.currentUser().subscribe(user => this.user = user);
    productsService.getActiveCatalog().subscribe((catalog) => {
      this.activeCatalog = catalog;
      this.title = `Catalog «${this.activeCatalog.name}»`;
      if (this.isCreateMode) {
        this.title += '/ choose products for order';
      }
    });
  }

  canNext = () => !this.activeCatalog.products.filter(p => p.selected).length;

  canEdit = () => CatalogGuard.check(this.user);

  handleNext = () => {
    console.log(this.activeCatalog.products);
    CatalogComponent.selectedProducts = this.activeCatalog.products.filter(p => p.selected);
  }
}
