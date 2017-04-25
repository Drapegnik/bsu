import { Component } from '@angular/core';
import User from '../_models/user';
import { AuthenticationService } from '../_sevices/authentication.service';

@Component({
  selector: 'app-home',
  template: `<h2>Hello, {{user.firstName}} {{user.lastName}}!</h2>`
})
export class HomeComponent {
  user: User;

  constructor(private authenticationService: AuthenticationService) {
    authenticationService.currentUser().subscribe(user => this.user = user);
  }
}
