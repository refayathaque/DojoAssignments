import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Switchboard';

  count1: number = 0;
  count2: number = 0;
  count3: number = 0;
  count4: number = 0;

  toggle1(){
    this.count1++
    console.log('Button has been toggled!')
  }
  toggle2(){
    this.count2++
    console.log('Button has been toggled!')
  }
  toggle3(){
    this.count3++
    console.log('Button has been toggled!')
  }
  toggle4(){
    this.count4++
    console.log('Button has been toggled!')
  }
}
