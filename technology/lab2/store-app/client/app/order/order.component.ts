import { Component } from '@angular/core';
import { FormBuilder, Validators, AbstractControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import {OrderService} from '../_sevices/order.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  // styleUrls: ['./order.component.css']
})
export class OrderComponent {
  form: FormGroup;
  product: AbstractControl;
  quantity: AbstractControl;
  customer: AbstractControl;

  constructor(private router: Router,
              private fb: FormBuilder,
              private orderService: OrderService) {
    this.form = fb.group({
      'product': ['', Validators.required],
      'quantity': ['', Validators.required],
      'customer': ['', Validators.required]
    });
    this.product = this.form.controls['product'];
    this.quantity = this.form.controls['quantity'];
    this.customer = this.form.controls['customer'];

  }

  create() {
    this.orderService.create(this.product.value, this.quantity.value, this.customer.value).subscribe(
      () => this.router.navigate(['/']),
      err => console.error(err));
  }


}
