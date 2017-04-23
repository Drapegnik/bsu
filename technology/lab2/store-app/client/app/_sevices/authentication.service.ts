﻿import {Injectable} from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs';

@Injectable()
export class AuthenticationService {

  static isLogged = false;
  private authUrl = 'http://localhost:3000/auth/';

  constructor(private http: Http) {
  };

  login(username: string, password: string) {
    return this.http.post(this.authUrl + 'login', {username: username, password: password})
      .map((response: Response) => {
        if (response.status === 200) {
          AuthenticationService.isLogged = true;
        }
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }

  logout() {
    return this.http.get(this.authUrl + 'logout')
      .map(() => AuthenticationService.isLogged = false)
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }
}
