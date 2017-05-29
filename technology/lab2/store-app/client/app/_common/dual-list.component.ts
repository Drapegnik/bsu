/**
 * Created by Drapegnik on 5/29/17.
 */

import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-dual-list',
  templateUrl: './dual-list.component.html'
})
export class DualListComponent implements OnInit {
  @Input() returnLink: string;
  @Input() saveCallback: Function;
  @Input() left: {
    title: string,
    data: Array<Object>,
  };
  @Input() right: {
    title: string,
    data: Array<Object>,
  };
  leftSelected: Array<{ selected: boolean }>;
  rightSelected: Array<{ selected: boolean }>;


  constructor() {
    this.leftSelected = [];
    this.rightSelected = [];
  }

  ngOnInit() {
    this.left.data = this.filter(this.right.data, this.left.data);
  }

  private filter(data, from) {
    return from.filter(({ id }) => !data.map(d => d.id).includes(id));
  }

  moveToRight() {
    this.leftSelected.forEach(item => item.selected = false);
    this.left.data = this.filter(this.leftSelected, this.left.data);
    this.right.data = this.right.data.concat(this.leftSelected);
    this.leftSelected = [];
  }

  moveToLeft() {
    this.rightSelected.forEach(item => item.selected = false);
    this.right.data = this.filter(this.rightSelected, this.right.data);
    this.left.data = this.left.data.concat(this.rightSelected);
    this.rightSelected = [];
  }
}
