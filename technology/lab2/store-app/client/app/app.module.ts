import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { NavbarComponent } from './navbar/navbar.component';
import { OrderComponent } from './order/order.component';

import { OrdersPageComponent } from './order/orders.page.component';
import { CatalogComponent } from './catalog/catalog.component';

import { AuthGuard } from './_guards/auth.guard';
import { AuthenticationService } from './_sevices/authentication.service';
import { OrderService } from './_sevices/order.service';
import { ProductService } from './_sevices/product.service';

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
    OrderService,
    ProductService,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {
}
