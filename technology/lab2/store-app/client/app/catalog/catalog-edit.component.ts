/**
 * Created by Drapegnik on 5/29/17.
 */

import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { ProductsService } from '../_sevices/products.service';
import Catalog from '../_models/catalog';

@Component({
  selector: 'app-catalog-edit',
  template: `
    <app-dual-list
      *ngIf="left && right"
      [left]="left"
      [right]="right"
      [returnLink]="'/catalog'"
      [saveCallback]="save"
    ></app-dual-list>
  `
})
export class CatalogEditComponent {
  left: {
    title: string,
    data: Array<Object>,
  };
  right: {
    title: string,
    data: Array<Object>,
  };
  catalog: Catalog;

  constructor(private productsService: ProductsService, private router: Router) {
    productsService.getAll().subscribe((products) => {
      this.left = {
        title: 'Products',
        data: products,
      };
    });

    productsService.getActiveCatalog().subscribe((catalog) => {
      console.log(catalog);
      this.catalog = catalog;
      this.right = {
        title: `Catalog «${catalog.name}»`,
        data: catalog.products,
      };
    });

    this.save = this.save.bind(this);
  }

  save(result) {
    console.log(this);
    console.log(result);
    this.catalog.products = result;
    this.productsService.saveCatalog(this.catalog).subscribe(
      () => {
        this.router.navigate(['/catalog']);
      },
      (err) => {
        console.error(`Error: ${err._body}`);
      });
  }
}
