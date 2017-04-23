import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class OrderService {

  private orderUrl = 'http://localhost:3000/order/';

  constructor(private http: Http) {
  };

  getAll() {
    return this.http.get(this.orderUrl + 'all')
      .map((response: Response) => {
        if (response.status === 200) {
          /**/
        }
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }

  create(product: string, quantity: string, customer: string) {
    return this.http.post(this.orderUrl + 'create', { product: product, quantity: quantity, customer: customer })
      .map(() => {

      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }
}
