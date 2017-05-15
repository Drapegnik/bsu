import { Component } from '@angular/core';

import Order from '../_models/order';
import { OrderService } from '../_sevices/order.service';

@Component({
  selector: 'app-orders',
  template: `
    <div *ngFor="let order of orders; let i=index">
      <app-order-item [index]="i" [order]="order"></app-order-item>
    </div>
  `
})
export class OrdersPageComponent {
  orders: Array<Order>;

  constructor(private orderService: OrderService) {
    orderService.getAll().subscribe(orders => this.orders = orders);
  }
}
