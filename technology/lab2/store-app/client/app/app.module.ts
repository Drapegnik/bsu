import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { CatalogComponent } from './catalog/catalog.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { NavbarComponent } from './navbar/navbar.component';
import { OrderComponent } from './orders/order.component';
import { OrderFormComponent } from './orders/order-form.component';
import { OrdersPageComponent } from './orders/orders-page.component';

import { AuthGuard } from './_guards/auth.guard';
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
    path: 'orders/create',
    component: CatalogComponent,
    canActivate: [AuthGuard], // todo: add roles checking,
    data: { isCreateMode: true },
  },
  {
    path: 'orders/create/form',
    component: OrderFormComponent,
    canActivate: [AuthGuard], // todo: add roles checking,
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
    NavbarComponent,
    LoginUserComponent,
    OrdersPageComponent,
    OrderComponent,
    OrderFormComponent,
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
    OrdersService,
    ProductsService,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {
}
