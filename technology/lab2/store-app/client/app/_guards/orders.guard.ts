/**
 * Created by Drapegnik on 5/29/17.
 */

import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot } from '@angular/router';

import { AuthenticationService } from '../_sevices/authentication.service';
import User from '../_models/user';

@Injectable()
export class OrdersGuard implements CanActivate {
  user: User;

  constructor(private router: Router, private authenticationService: AuthenticationService) {
    authenticationService.currentUser().subscribe(user => this.user = user);
  }

  canActivate(route: ActivatedRouteSnapshot,
              state: RouterStateSnapshot) {

    if (this.user.role === 'admin' || this.user.role === 'order-manager') {
      return true;
    }

    this.router.navigate(['orders']);
    return false;
  }
}
