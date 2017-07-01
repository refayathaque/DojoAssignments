import { Component, OnInit } from '@angular/core';
import { Cookie } from "ng2-cookies";
import { Router } from "@angular/router";
import { LoginRegistrationService } from "app/loginregistration.service";
import { BucketList } from '../bucketlist'; // MUST IMPORT CONSTRUCTOR CLASSES
import { ActivatedRoute } from "@angular/router"; // MUST IMPORT FOR PASSING ID IN URL

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {

    username = Cookie.get('logged_username')

    constructor(private _LoginRegistrationService: LoginRegistrationService, private _Router: Router, _activatedRoute: ActivatedRoute) { } // Dependency Injections for some IMPORTS

    users = [];

    bucketlists = [];

  ngOnInit() {
      this._LoginRegistrationService.listallusers()
      .then(data => {
          this.users = data
          console.log(this.users)
      })
      .catch(err => console.log(err))

      this._LoginRegistrationService.listallbucketlists()

  }

  bucketlist = new BucketList();

  useraddingtobucketlist = "";

  onChange(newValue) {
      console.log(newValue);
      this.useraddingtobucketlist = newValue;
  }

  addbucketlist() {
      this.bucketlist.users = this.useraddingtobucketlist
      console.log('USERS : ', this.bucketlist.users)
      this.bucketlist.created_by = Cookie.get('logged_username');
      console.log('BucketList Component Before Service Call', this.bucketlist)
      this._LoginRegistrationService.addbucketlist(this.bucketlist)
      .then((data) => {
          if(data) {
              alert(data.messages)
              this._Router.navigateByUrl('home')
              // Route worked bc just 'data' was passed in above in if statement, not 'data.question' or 'data.content'
          } else {
              alert(data.messages)
          }
      })
      .catch((err) => {
      console.log("ERR Inside Question Component")
      console.log(err)
      })
  }

  logout() {
      Cookie.deleteAll()
      this._Router.navigateByUrl('login')
  }

}
