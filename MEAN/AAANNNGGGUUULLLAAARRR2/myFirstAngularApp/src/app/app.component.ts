import { Component } from '@angular/core';
import { User } from './user';

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
  // user: object = {
  //   f_name: 'Refayat',
  //   l_name: 'Haque'
  // }
  today = new Date();
  myBoolean = true;
  myArray: Array<string> = ['Camry', 'Accord', 'Malibu', 'Fusion'];
  num = 1;
	logNum(){
		console.log("num is: ", this.num);
	}
  increaseNum(){
    this.num = this.num + 2;
  }
  users = [];
  user = {
    firstName: '',
    lastName: '',
    password: ''
  }
  onSubmit(){
    console.log('onSubmit()');
    console.log(this.user);
    this.users.push(this.user); // Pushing REFERENCE of that object
    this.user = {
      firstName: '',
      lastName: '',
      password: ''
    }
    // ^ Redefining user variable to be a NEW INSTANCE of an object. So now it's a clean empty object that is not the same.
  }
}
