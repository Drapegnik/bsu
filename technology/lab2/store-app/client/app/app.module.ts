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
import { OrderComponent } from 'app/order/order.component';


const orderRoutes: Routes = [

  { path: 'createorder', component: OrderComponent },

];

const appRoutes: Routes = [
  { path: '', component: HomeComponent, children: orderRoutes, canActivate: [AuthGuard] },
  { path: 'login', component: LoginUserComponent },
  { path: '**', redirectTo: '' },
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
