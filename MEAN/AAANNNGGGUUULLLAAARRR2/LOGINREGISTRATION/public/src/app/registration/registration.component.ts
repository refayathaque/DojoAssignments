import { Component, OnInit } from '@angular/core';
import { User } from '../user'; // MUST IMPORT CONSTRUCTOR CLASSES
import { LoginRegistrationService } from "app/loginregistration.service";
import { Router } from "@angular/router";
import { Cookie } from 'ng2-cookies';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})

export class RegistrationComponent implements OnInit {

  constructor(private _LoginRegistrationService: LoginRegistrationService, private _Router:Router) { }

  user = new User();
  
  ngOnInit() { }

  registration() {
      if (this.user.password !== this.user.confirmpassword) {
          alert("Passwords do not match!") }
      else
      {
          this._LoginRegistrationService.registerUser(this.user)
          .then((data) => {
              if(data.error) {
                  alert(data.messages)
              } else {
                  console.log("DATA Inside Register Component")
                  console.log(data)
              }
          })
          .catch((err) => {
          console.log("ERR Inside Register Component")
          console.log(err)
          })
      }
  }

}
