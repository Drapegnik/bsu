import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { CatalogComponent } from './catalog/catalog.component';
import { CatalogEditComponent } from './catalog/catalog-edit.component';
import { CircleBtnComponent } from './_common/circle-btn.component';
import { DualListComponent } from './_common/dual-list.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { NavbarComponent } from './navbar/navbar.component';
import { OrderComponent } from './orders/order.component';
import { OrderFormComponent } from './orders/order-form.component';
import { OrdersPageComponent } from './orders/orders-page.component';
import { ProductsTableComponent } from './products/products-table.component';
import { ProductsPageComponent } from './products/proucts-page.component';

import { AuthGuard } from './_guards/auth.guard';
import { OrdersGuard } from './_guards/orders.guard';
import { ProductsGuard } from './_guards/products.guard';
import { CatalogGuard } from './_guards/catalog.guard';

import { AuthenticationService } from './_sevices/authentication.service';
import { OrdersService } from './_sevices/orders.service';
import { ProductsService } from './_sevices/products.service';

const appRoutes: Routes = [
  {
    path: 'orders',
    component: OrdersPageComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'catalog',
    component: CatalogComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'catalog/edit',
    component: CatalogEditComponent,
    canActivate: [AuthGuard, CatalogGuard]
  },
  {
    path: 'orders/create',
    component: CatalogComponent,
    canActivate: [AuthGuard, OrdersGuard],
    data: { isCreateMode: true },
  },
  {
    path: 'orders/create/form',
    component: OrderFormComponent,
    canActivate: [AuthGuard, OrdersGuard],
  },
  {
    path: 'products',
    component: ProductsPageComponent,
    canActivate: [AuthGuard, ProductsGuard],
  },
  {
    path: 'login',
    component: LoginUserComponent
  },
  {
    path: '**',
    redirectTo: 'orders'
  },
];

@NgModule({
  declarations: [
    AppComponent,
    CatalogComponent,
    CatalogEditComponent,
    CircleBtnComponent,
    DualListComponent,
    NavbarComponent,
    LoginUserComponent,
    OrdersPageComponent,
    OrderComponent,
    OrderFormComponent,
    ProductsTableComponent,
    ProductsPageComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    AlertModule.forRoot(),
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
  ],
  providers: [
    AuthGuard,
    AuthenticationService,
    CatalogGuard,
    OrdersGuard,
    OrdersService,
    ProductsGuard,
    ProductsService,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {
}
