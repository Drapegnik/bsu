import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { OrdersController } from './order/orders.controller';
import { NavbarComponent } from './navbar/navbar.component';
import { OrderComponent } from './order/order.component';

import { AuthGuard } from './_guards/auth.guard';
import { AuthenticationService } from './_sevices/authentication.service';
import { OrderService } from './_sevices/order.service';

const appRoutes: Routes = [
  {
    path: 'orders',
    component: OrdersController,
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
    NavbarComponent,
    LoginUserComponent,
    OrdersController,
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
  ],
  bootstrap: [AppComponent],
})
export class AppModule {
}
