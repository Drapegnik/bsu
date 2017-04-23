import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

@Injectable()
export class AuthenticationService {
    constructor(private http: Http) { };

    /*вот тут придумать логику*/
    login(username: string, password: string) {
        return this.http.post('/api/authenticate', JSON.stringify({ username: username, password: password }))
            .map((response: Response) => {
            const user = response.json(); /*вот тут обработать, залогинился */
                if (user ) {
                    localStorage.setItem('currentUser', JSON.stringify(user));
                }
            });
    }

    logout() {
       /*и тут*/
        localStorage.removeItem('currentUser');
    }
}
