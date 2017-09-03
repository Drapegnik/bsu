/**
 * Created by Drapegnik on 5/29/17.
 */

import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-circle-btn',
  template: `
    <div class="col-md-1 col-xs-1">
      <a [routerLink]="[link]"><span class="hvr-pulse-grow circle-btn {{iconClass}}"></span></a>
    </div>
  `,
  styles: [`
    .circle-btn {
      font-size: 80px;
      color: #2a9fd6;
      position: fixed;
      z-index: 1;
      right: 4%;
      top: 88%
    }

    @media only screen and (max-width: 320px) {
      .circle-btn {
        font-size: 30px;
        right: 2%;
      }
    }

    @media only screen and (max-width: 767px) {
      .circle-btn {
        font-size: 40px;
        right: 3%;
      }
    }
  `]
})
export class CircleBtnComponent {
  @Input() link: string;
  @Input() iconClass: string;
}
