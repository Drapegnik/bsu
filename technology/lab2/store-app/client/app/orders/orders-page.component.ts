import { Component } from '@angular/core';

import Order from '../_models/order';
import User from '../_models/user';
import { OrdersService } from '../_sevices/orders.service';
import { AuthenticationService } from '../_sevices/authentication.service';
import { OrdersGuard } from '../_guards/orders.guard';

@Component({
  selector: 'app-orders-page',
  template: `
    <div *ngFor="let order of orders; let i=index">
      <app-order [index]="i" [order]="order"></app-order>
    </div>
    <app-circle-btn
      *ngIf="canCreate()"
      [link]="'create'"
      [iconClass]="'glyphicon glyphicon-plus-sign'"
    ></app-circle-btn>
  `,
})
export class OrdersPageComponent {
  orders: Array<Order>;
  user: User;

  constructor(private ordersService: OrdersService, private authenticationService: AuthenticationService) {
    ordersService.getAll().subscribe(orders => this.orders = orders.reverse());
    authenticationService.currentUser().subscribe(user => this.user = user);
  }

  canCreate() {
    return OrdersGuard.check(this.user);
  }
}
