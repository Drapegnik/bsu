import { Component } from '@angular/core';
import { FormBuilder, Validators, AbstractControl, FormGroup } from '@angular/forms';
import { AuthenticationService } from '../_sevices/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css']
})
export class LoginUserComponent {
  form: FormGroup;
  username: AbstractControl;
  password: AbstractControl;

  constructor(private router: Router,
              private fb: FormBuilder,
              private authenticationService: AuthenticationService) {
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
    this.username = this.form.controls['username'];
    this.password = this.form.controls['password'];
  }

  login() {
    this.authenticationService.login(this.username.value, this.password.value).subscribe(
      () => this.router.navigate(['']),
      err => console.error(err));
  }

  loginVia(provider: string) {
  }
}
