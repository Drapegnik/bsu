import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { ReplaySubject } from 'rxjs/ReplaySubject';
import 'rxjs/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';

import User from '../_models/user';

@Injectable()
export class AuthenticationService {

  static isLogged = false;
  private authUrl = 'http://localhost:3000/auth/';
  private userSubject: ReplaySubject<User>;

  constructor(private http: Http) {
    this.initUserSubject();
  };

  login(username: string, password: string) {
    return this.http.post(this.authUrl + 'login', { username: username, password: password })
      .map((response: Response) => {
        if (response.status === 200) {
          AuthenticationService.isLogged = true;
          this.userSubject.next(new User(JSON.parse(response['_body'])));
        }
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }

  logout() {
    return this.http.get(this.authUrl + 'logout')
      .map((response: Response) => {
        console.log(response);
        this.userSubject.next(new User({ isAnonymous: true }));
        AuthenticationService.isLogged = false;
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }

  private initUserSubject() {
    this.userSubject = new ReplaySubject<User>(1);
    this.userSubject.next(new User({ isAnonymous: true }));
  }

  currentUser(): Observable<User> {
    return this.userSubject.asObservable();
  }
}
