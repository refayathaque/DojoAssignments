import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import 'rxjs/RX'; // RxJS stands for *R*eactive E*x*tensions for *J*ava*S*cript, and its a library that gives us an implementation of Observables for JS

@Injectable()
export class LoginRegistrationService {

  constructor(private _Http: Http) { }

  registerUser(user){
    console.log(user)
    return this._Http.post('/users', user)
    .map((data) => {
      console.log("data", data)
      return data.json()
    })
    .toPromise();
  }
}
