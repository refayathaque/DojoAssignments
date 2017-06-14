import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dojo Mail';
  emails = [{email: ["bill@gates.com", "ada@lovelace.com", "john@carmac.com", "gabe@newel.com"]}, {importance: [true, true, false, false]}, {subject:["So Tired!", "Must Sleep!", "Hungry As Well!", "Going Home Soon!"]}, {content:["Windows XI will launch in year 2100.", "Enchantress of Numbers", "New algorithm for shadow volumes.", "Just kidding..."]}]
}
