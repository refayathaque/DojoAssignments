import { Component, OnInit } from '@angular/core';
import { Cookie } from "ng2-cookies";
import { Router } from "@angular/router";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {

    username = Cookie.get('logged_username')

  constructor(private _Router: Router) { }

  ngOnInit() {
  }

  logout() {
      Cookie.deleteAll()
      this._Router.navigateByUrl('login')
  }

  addquestion() {
      this._Router.navigateByUrl('question')
  }

}
