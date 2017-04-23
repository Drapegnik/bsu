import { Component } from '@angular/core';
import { AuthenticationService } from '../_sevices/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html'
})
export class NavbarComponent {

  constructor(private router: Router,
              private authenticationService: AuthenticationService) {
  }

  logout() {
    this.authenticationService.logout().subscribe(
      () => this.router.navigate(['/login']),
      err => console.error(err));
  }
}
