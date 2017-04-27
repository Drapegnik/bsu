import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { ReplaySubject } from 'rxjs/ReplaySubject';
import 'rxjs/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';

import User from '../_models/user';
import SettingsService from '../settings.servise';

@Injectable()
export class AuthenticationService {

  static isLogged = false;
  private userSubject: ReplaySubject<User>;

  constructor(private http: Http) {
    this.initUserSubject();
  };

  private handleUserResponse = (response: Response) => {
    if (response.status === 200) {
      AuthenticationService.isLogged = true;
      this.userSubject.next(new User(JSON.parse(response['_body'])));
    }
    return response;
  }

  private handleErrorResponse = (error: any) => {
    console.log(error);
    return Observable.throw(error || 'Server error');
  }

  loadCurrentUser() {
    return this.http.get(`${SettingsService.apiUrl}/users/me`)
      .map(this.handleUserResponse)
      .catch(this.handleErrorResponse);
  }

  login(username: string, password: string) {
    return this.http.post(`${SettingsService.authUrl}/login`, { username: username, password: password })
      .map(this.handleUserResponse)
      .catch(this.handleErrorResponse);
  }

  logout() {
    return this.http.get(`${SettingsService.authUrl}/logout`)
      .map(() => {
        this.userSubject.next(new User({ isAnonymous: true }));
        AuthenticationService.isLogged = false;
      })
      .catch(this.handleErrorResponse);
  }

  private initUserSubject() {
    this.userSubject = new ReplaySubject<User>(1);
    this.userSubject.next(new User({ isAnonymous: true }));
  }

  currentUser(): Observable<User> {
    return this.userSubject.asObservable();
  }
}
