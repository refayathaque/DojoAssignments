import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'My First Component Test';
  x: number = 5;
  y: number = 9;
  myStr: string = "abc";
  user: object = {
    f_name: 'Refayat',
    l_name: 'Haque'
  }
  today = new Date();
  myBoolean = true;
  myArray: Array<string> = ['Camry', 'Accord', 'Malibu', 'Fusion'];
}
