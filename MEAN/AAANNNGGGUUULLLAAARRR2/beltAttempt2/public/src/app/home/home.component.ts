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

    constructor(private _LoginRegistrationService: LoginRegistrationService, private _Router: Router, _activatedRoute: ActivatedRoute) { } // Dependency Injections for some IMPORTS

    // Variables
    username = Cookie.get('logged_username')
    all_users = []; // To display ALL users in bucketlist form's dropdown menu
    all_items = []; // ALL bucket list items in db
    session_user_items = []; // Session user's bucket list items

  ngOnInit() {
      // Populates 'all_users' array for bucket list form's dropdown menu
      this._LoginRegistrationService.show_all_users()
      .then(data => {
          this.all_users = data
      })
      .catch(err => console.log(err))

      // Populates 'all_items' array, 'all_items' is SORTed in the following function, then we will have only the items beloging to the user logged in (inside 'session_user_items' array)
      this._LoginRegistrationService.show_all_items()
      .then(data => {
          this.all_items = data
          sort(this.all_items, this.session_user_items);
          // IMPORTANT to pass in the array we will be iterating over AS WELL AS the array we will be populating, in this case the 'session_user_items' array
      })
      .catch(err => console.log(err))

      function sort(array1, array2) {
          for(var i = 0; i < array1.length; i++){
              console.log(array1[i].created_by);
              if(array1[i].created_by === Cookie.get('logged_username')) {
              // Change to 'logged_id' after changing code for creating new bucket list item
                  array2.push(array1[i]);
                  console.log(array2);
              }
          }
      }

  }

  bucketlist = new BucketList(); // INSTANTIATING class for new bucket list entries

  // Getting friend's ID value
  friend_id = "";
  friend_username = "";
  onChange() {
      for(var i = 0; i < this.all_users.length; i++) {
          if(this.all_users[i].username === this.friend_username) {
              this.friend_id = this.all_users[i]._id
              console.log('Friend ID: ', this.friend_id)
          }
      }
  }

  // Adding bucket list item to db
  add_item() {
      this.bucketlist.friend = this.friend_id
      console.log('Bucket list friend ID: ', this.bucketlist.friend)
      this.bucketlist.created_by = Cookie.get('logged_id');
      console.log('Bucket list component before service call', this.bucketlist)
      this._LoginRegistrationService.add_item(this.bucketlist)
      .then((data) => {
          if(data) {
              console.log(data);
              alert(data.messages)
              this._Router.navigateByUrl('home')
              // Route worked bc just 'data' was passed in above in if statement, not 'data.question' or 'data.content'
              this.session_user_items.push(data.bucketlist)
              // ^ Updates the session_user_bucket_list_items array to include item just added by this function
              // session_user_bucket_list_items is TEMPORARY, that's why this works and why we don't get repeats in the table
          } else {
              alert(data.messages)
          }
      })
      .catch((err) => {
      console.log("ERR Inside Home Component")
      console.log(err)
      })
  }

  updatebucketlist(id) {
      console.log('CHECK BOX WORKS', id)
      this._LoginRegistrationService.updatebucketlist(id)
      .then(data => {
          for(var i = 0; i < this.session_user_items.length; i++) {
              if(this.session_user_items[i]._id === data._id && this.session_user_items[i].status === false) {
                  this.session_user_items[i].status = true;
              }
              else if(this.session_user_items[i]._id === data._id && this.session_user_items[i].status === true) {
                  this.session_user_items[i].status = false;
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
