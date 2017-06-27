import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies';
import { Router } from "@angular/router";
import { LoginRegistrationService } from "app/loginregistration.service";
import { User } from '../user'; // MUST IMPORT CONSTRUCTOR CLASSES

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private _LoginRegistrationService: LoginRegistrationService, private _Router:Router) { }

  user = new User();

  ngOnInit() {
  }

  login() {
    console.log(this.user)
    this._LoginRegistrationService.loginUser(this.user)
    .then((data) => {
      if(data.login) {
        alert("You are logged in!")
        Cookie.set("logged_id", data.user._id)
      } else {
        alert(data.error)
      }
    })
  }

}
