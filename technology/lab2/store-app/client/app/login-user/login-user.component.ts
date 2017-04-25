import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, AbstractControl, FormGroup } from '@angular/forms';
import { AuthenticationService } from '../_sevices/authentication.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css'],
})
export class LoginUserComponent implements OnInit {
  form: FormGroup;
  username: AbstractControl;
  password: AbstractControl;
  errors: Object;
  returnUrl: string;

  constructor(private route: ActivatedRoute,
              private router: Router,
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

  ngOnInit() {
    if (AuthenticationService.isLogged) {
      this.router.navigate(['home']);
    }
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || 'home';
  }

  login() {
    this.authenticationService.login(this.username.value, this.password.value).subscribe(
      () => {
        this.errors = {};
        this.router.navigate([this.returnUrl]);
      },
      (err) => {
        this.errors = JSON.parse(err._body);
        console.error(`Error: ${err._body}`);
      });
  }

  loginVia(provider: string) {
  }
}
