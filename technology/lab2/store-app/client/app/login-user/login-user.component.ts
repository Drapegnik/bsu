import { Component } from '@angular/core';
import { FormBuilder, Validators, AbstractControl, FormGroup } from '@angular/forms';
import { AuthenticationService } from '../_sevices/authentication.service';
import { Router } from '@angular/router';
import { OrderService } from "../_sevices/order.service";

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css'],
  providers: [OrderService]
})
export class LoginUserComponent {
  form: FormGroup;
  username: AbstractControl;
  password: AbstractControl;
  errors: Object;

  constructor(private router: Router,
              private fb: FormBuilder,
              private authenticationService: AuthenticationService) {
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
    this.username = this.form.controls['username'];
    this.password = this.form.controls['password'];
    this.errors = {};
  }

  login() {
    this.authenticationService.login(this.username.value, this.password.value).subscribe(
      () => {
        this.errors = {};
        this.router.navigate(['']);
      },
      (err) => {
        this.errors = JSON.parse(err._body);
        console.error(`Error: ${err._body}`);
      });
  }

  loginVia(provider: string) {
  }
}
