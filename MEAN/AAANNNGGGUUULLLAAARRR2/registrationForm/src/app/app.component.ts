import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Registration';
  users = []
  user = {
    fname: '',
    lname: '',
    email: '',
    password: '',
    pconfirmation: '',
    address: '',
    apt: '',
    city: '',
    state: '',
    lucky: ''
  }
  onSubmit(){
    console.log('Submitted')
    this.users.push(this.user)
  }
}
