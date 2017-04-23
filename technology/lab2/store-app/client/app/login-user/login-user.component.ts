import {Component} from '@angular/core';
import {FormBuilder, Validators, AbstractControl, FormGroup} from '@angular/forms';
import {AuthenticationService} from '../_sevices/authentication.service';

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css']
})

export class LoginUserComponent {
  form: FormGroup;
  username: AbstractControl;
  password: AbstractControl;

  checking = '-----------';

  constructor(private fb: FormBuilder,
              private authenticationService: AuthenticationService) {
    this.form = fb.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required]
    });
    this.username = this.form.controls['username'];
    this.password = this.form.controls['password'];
  }

  login() {
      this.authenticationService.login(this.form.controls['username'].value, this.form.controls['password'].value);
      this.checking = 'login pressed';
  }

  loginVia(provider: string) {
  }
}
