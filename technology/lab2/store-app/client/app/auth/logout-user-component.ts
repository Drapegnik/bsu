import { Router } from '@angular/router';
import { AuthenticationService } from '../_sevices/authentication.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-logout-user',
  template: ``
})
export class LogoutUserComponent {
  constructor(private router: Router,
              private authenticationService: AuthenticationService) {

    this.authenticationService.logout().subscribe(
      () => this.router.navigate(['']),
      err => console.error(err));
  }
}
