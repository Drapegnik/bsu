import { Component } from '@angular/core';
import { AuthenticationService } from '../_sevices/authentication.service';
import { Router } from '@angular/router';
import User from '../_models/user';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html'
})
export class NavbarComponent {
  user: User;

  constructor(private router: Router,
              private authenticationService: AuthenticationService) {
    authenticationService.currentUser().subscribe(user => this.user = user);
  }

  logout() {
    this.authenticationService.logout().subscribe(
      () => this.router.navigate(['login']),
      err => console.error(err));
  }
}
