import { Component } from '@angular/core';

import Order from '../_models/order';
import User from '../_models/user';
import { OrdersService } from '../_sevices/orders.service';
import { AuthenticationService } from '../_sevices/authentication.service';

@Component({
  selector: 'app-orders-page',
  template: `
    <div *ngFor="let order of orders; let i=index">
      <app-order [index]="i" [order]="order"></app-order>
    </div>
    <div *ngIf="canCreate()" class="col-md-1 col-xs-1">
      <a [routerLink]="['create']"><span class="hvr-pulse-grow create glyphicon glyphicon-plus-sign"></span></a>
    </div>
  `,
  styles: [`
    .create {
      font-size: 80px;
      color: #2a9fd6;
      position: fixed;
      z-index: 1;
      right: 4%;
      top: 88%
    }

    @media only screen and (max-width: 320px) {
      .create {
        font-size: 30px;
        right: 2%;
      }
    }

    @media only screen and (max-width: 767px) {
      .create {
        font-size: 40px;
        right: 3%;
      }
    }
  `]
})
export class OrdersPageComponent {
  orders: Array<Order>;
  user: User;

  constructor(private ordersService: OrdersService, private authenticationService: AuthenticationService) {
    ordersService.getAll().subscribe(orders => this.orders = orders.reverse());
    authenticationService.currentUser().subscribe(user => this.user = user);
  }

  public canCreate() {
    return this.user.role === 'admin' || this.user.role === 'order-manager';
  }
}
