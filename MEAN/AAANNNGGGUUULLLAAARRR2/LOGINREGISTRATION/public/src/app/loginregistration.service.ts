import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import 'rxjs';

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
