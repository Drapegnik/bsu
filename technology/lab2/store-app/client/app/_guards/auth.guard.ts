import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthenticationService } from '../_sevices/authentication.service';

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (AuthenticationService.isLogged === true) {
      return true;
    }

    this.router.navigate(['/login'], {queryParams: {returnUrl: state.url}});
    return false;
  }
}
