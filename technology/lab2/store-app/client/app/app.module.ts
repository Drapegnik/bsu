<<<<<<< HEAD
import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {RouterModule, Routes} from '@angular/router';
import {AlertModule} from 'ngx-bootstrap';

import {AppComponent} from './app.component';
import {LoginUserComponent} from './auth/login-user.component';
import {HomeComponent} from './home/home.component';
import {AuthGuard} from './_guards/auth.guard';
import {AuthenticationService} from './_sevices/authentication.service';
import {LogoutUserComponent} from './auth/logout-user-component';
import {OrderComponent} from "app/order/order.component";


const orderRoutes: Routes = [

  {path: 'createorder', component: OrderComponent},

];

const appRoutes: Routes = [
  {path: '', component: HomeComponent, children: orderRoutes, canActivate: [AuthGuard]},
  {path: 'login', component: LoginUserComponent},
  {path: 'logout', component: LogoutUserComponent},
  {path: '**', redirectTo: ''},
=======
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { HomeComponent } from './home/home.component';
import { AuthGuard } from './_guards/auth.guard';
import { AuthenticationService } from './_sevices/authentication.service';
import { NavbarComponent } from './navbar/navbar.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginUserComponent },
  { path: '**', redirectTo: '' },
>>>>>>> 14a6d3e2152ac3693528123e7d1fa7a351331de8
];

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    LoginUserComponent,
    HomeComponent,
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
  ],

  bootstrap: [AppComponent],
})
export class AppModule {
}
