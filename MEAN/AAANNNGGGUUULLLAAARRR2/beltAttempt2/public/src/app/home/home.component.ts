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

    users = []; // For dropdown menu

    all_users_bucket_list_items = [];
    session_user_bucket_list_items = [];

  ngOnInit() {
      this._LoginRegistrationService.listallusers()
      .then(data => {
          this.users = data
          console.log(this.users)
      })
      .catch(err => console.log(err))

      this._LoginRegistrationService.userbucketlists()
      .then(data => {
          this.all_users_bucket_list_items = data
          console.log(this.all_users_bucket_list_items)
          extract_session_user_bucket_list_items(this.all_users_bucket_list_items, this.session_user_bucket_list_items);
          // IMPORTANT to pass in the array we will be iterating over AS WELL AS the array we will be populating, in this case the 'sessionuserbucketlists' array
      })
      .catch(err => console.log(err))

      function extract_session_user_bucket_list_items(array, array2) {
          for(var i = 0; i < array.length; i++){
              console.log(array[i].created_by);
              if(array[i].created_by === Cookie.get('logged_username')) {
                console.log('array[i] or BucketList item belonging to the user in session : ', array[i]);
                array2.push(array[i]);
                console.log(array2);
            }
          }
      }

  }

  bucketlist = new BucketList();

  useraddingtobucketlist = "";

  onChange(newValue) {
      console.log(newValue);
      this.useraddingtobucketlist = newValue;
  }

  addbucketlist() {
      this.bucketlist.friend = this.useraddingtobucketlist
      console.log('USERS : ', this.bucketlist.friend)
      this.bucketlist.created_by = Cookie.get('logged_username');
      console.log('BucketList Component Before Service Call', this.bucketlist)
      this._LoginRegistrationService.addbucketlist(this.bucketlist)
      .then((data) => {
          if(data) {
              console.log(data);
              alert(data.messages)
              this._Router.navigateByUrl('home')
              // Route worked bc just 'data' was passed in above in if statement, not 'data.question' or 'data.content'
              this.session_user_bucket_list_items.push(data.bucketlist)
              // ^ Updates the session_user_bucket_list_items array to include item just added by this function
              // session_user_bucket_list_items is TEMPORARY, that's why this works and why we don't get repeats in the table
          } else {
              alert(data.messages)
          }
      })
      .catch((err) => {
      console.log("ERR Inside Question Component")
      console.log(err)
      })

  }

  updatebucketlist(id) {
      console.log('CHECK BOX WORKS', id)
      this._LoginRegistrationService.updatebucketlist(id)
      .then(data => {
          for(var i = 0; i < this.session_user_bucket_list_items.length; i++) {
              if(this.session_user_bucket_list_items[i]._id === data._id && this.session_user_bucket_list_items[i].status === false) {
                  this.session_user_bucket_list_items[i].status = true;
              }
              else if(this.session_user_bucket_list_items[i]._id === data._id && this.session_user_bucket_list_items[i].status === true) {
                  this.session_user_bucket_list_items[i].status = false;
              }
          }
      })
      // ^ For loop to toggle 'true's to 'false's and vice versa in TEMPORARY array 'session_user_bucket_list_items', done to display changes made by user
      .catch(err => console.log(err))
  }

  logout() {
      Cookie.deleteAll()
      this._Router.navigateByUrl('login')
  }

}
