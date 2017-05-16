import { Component, Input } from '@angular/core';

import Order from '../_models/order';

/**
 * Created by Drapegnik on 5/15/17.
 */

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent {
  @Input() order: Order;
  @Input() index: Number;
}
