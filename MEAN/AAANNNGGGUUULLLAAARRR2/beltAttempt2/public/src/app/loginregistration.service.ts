import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import 'rxjs/RX'; // RxJS stands for *R*eactive E*x*tensions for *J*ava*S*cript, and its a library that gives us an implementation of Observables for JS

@Injectable()
export class LoginRegistrationService {

  constructor(private _Http: Http) { }

  // Registration
  registerUser(user) {
    console.log(user)
    return this._Http.post('/registration', user)
    .map((data) => {
      console.log("Inside Service (Registration) After HTTP Call")
      console.log("data", data)
      return data.json()
    })
    .toPromise();
  }

  // Login
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

  // Show all users in db
  show_all_users() {
      return this._Http.get('/show_all_users')
      .map((data) => {
          console.log("Data being returned to component", data)
          return data.json()
      })
      .toPromise();
  }

  // Show all bucket list items in db
  show_all_items() {
      return this._Http.get('/show_all_items')
      .map((data) => {
          console.log("Data being returned to component", data)
          return data.json()
      })
      .toPromise();
  }

  // Adds bucket list item to db
  add_item(bucketlist) {
      console.log('Bucket list adding in service', bucketlist)
      return this._Http.post('/create_item', bucketlist)
      .map((data) => {
          console.log("Inside service (bucket list) after HTTP call")
          console.log("Data being returned to component", data)
      return data.json()
    })
    .toPromise();
  }



  updatebucketlist(id) {
      return this._Http.post(`/updatebucketlist/${id}`, {id: id})
      .map((data) => {
          console.log("Data being returned to component", data)
          return data.json()
      })
      .toPromise()
  }

}
