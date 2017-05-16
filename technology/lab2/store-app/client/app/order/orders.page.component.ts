import { Component } from '@angular/core';

import Order from '../_models/order';
import { OrderService } from '../_sevices/order.service';

@Component({
  selector: 'app-orders-page',
  template: `
    <div *ngFor="let order of orders; let i=index">
      <app-order [index]="i" [order]="order"></app-order>
    </div>
    <div class="col-md-1 col-xs-1">
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

  constructor(private orderService: OrderService) {
    orderService.getAll().subscribe(orders => this.orders = orders);
  }
}
