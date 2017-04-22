import { Component } from '@angular/core';
import { FormBuilder, Validators, AbstractControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css']
})

export class LoginUserComponent {
  form: FormGroup;
  username: AbstractControl;
  password: AbstractControl;

  constructor(private fb: FormBuilder) {
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
    this.username = this.form.controls['username'];
    this.password = this.form.controls['password'];
  }

  login() {}

  loginVia(provider: string) {}
}
