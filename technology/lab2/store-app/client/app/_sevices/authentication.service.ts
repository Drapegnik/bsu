import {Injectable} from '@angular/core';
import {Http, Response} from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class AuthenticationService {

  static isLogged = false;

  constructor(private http: Http) {
  };
  /*вот тут получи свой респонс по нужному урлу твоего севрера и обработай  /--можещь закомментить все, кроме строчки  AuthenticationService.isLogged = true; и посмотреть как работает--/  */
  login(username: string, password: string) {
    return this.http.post('/', JSON.stringify({username: username, password: password}))
      .map((response: Response) => {
        const code = response.json();
        /*заглушка*/
        if (true /*code === '200'*/) {
          AuthenticationService.isLogged = true;
        }
      });
  }

  logout() {
    /*и тут*/
    AuthenticationService.isLogged = false;
  }
}
