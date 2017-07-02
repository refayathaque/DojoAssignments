import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import 'rxjs/RX'; // RxJS stands for *R*eactive E*x*tensions for *J*ava*S*cript, and its a library that gives us an implementation of Observables for JS

@Injectable()
export class LoginRegistrationService {

  constructor(private _Http: Http) { }

  registerUser(user) {
    console.log(user)
    return this._Http.post('/users', user)
    .map((data) => {
      console.log("Inside Service (Registration) After HTTP Call")
      console.log("data", data)
      return data.json()
    })
    .toPromise();
  }

  loginUser(user) {
    console.log(user)
    return this._Http.post('/login', user)
    .map((data) => {
      console.log("Inside Service (Login) After HTTP Call")
      console.log(data)
      return data.json()
    })
    .toPromise();
  }

  addbucketlist(bucketlist) {
      console.log('BucketList in Service', bucketlist)
      return this._Http.post('/addbucketlist', bucketlist)
      .map((data) => {
          console.log("Inside Service (BucketList) After HTTP Call")
          console.log("Data being returned to component", data)
      return data.json()
    })
    .toPromise();
  }

  listallusers() {
      return this._Http.get('/listallusers')
      .map((data) => {
          console.log("Data being returned to component", data)
          return data.json()
      })
      .toPromise();
  }

  userbucketlists() {
      return this._Http.get('/userbucketlists')
      .map((data) => {
          console.log("Data being returned to component", data)
          return data.json()
      })
      .toPromise();
  }

}
