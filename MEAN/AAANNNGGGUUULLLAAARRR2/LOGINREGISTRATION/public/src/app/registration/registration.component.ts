import { Component, OnInit } from '@angular/core';
import { User } from '../user'; // MUST IMPORT CONSTRUCTOR CLASSES

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  constructor() { }

  user = new User();
  users = [];
  registration() {
      console.log(this.user)
      this.users.push(this.user);
      this.user = new User();
  }

  ngOnInit() {
  }

}
