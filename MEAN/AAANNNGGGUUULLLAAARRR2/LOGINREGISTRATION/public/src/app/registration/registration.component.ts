import { Component, OnInit } from '@angular/core';
import { User } from '../user'; // MUST IMPORT CONSTRUCTOR CLASSES

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  constructor() {
      // Try doing date validation later. In HTML date input there should be min='{{ mindate }}'
      // Here there should be a function invoked on page load that takes the current date and subtracts accordingly to only allow people of a certain age to register. 
  }

  user = new User();
  users = [];
  registration() {
      console.log(this.user)
      this.users.push(this.user);
      this.user = new User();
  }

  mindate: number;

  ngOnInit() {

  }

}
