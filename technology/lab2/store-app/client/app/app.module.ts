import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { HomeComponent } from './home/home.component';

const appRoutes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'login', component: LoginUserComponent},
  {path: '**', redirectTo: ''},
];

@NgModule({
  declarations: [
    AppComponent,
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
  bootstrap: [AppComponent],
})
export class AppModule {
}
