import { Component, OnInit } from '@angular/core';
import { Cookie } from "ng2-cookies";
import { Router } from "@angular/router";
import { LoginRegistrationService } from "app/loginregistration.service";
import { Question } from '../question'; // MUST IMPORT CONSTRUCTOR CLASSES
import { ActivatedRoute } from "@angular/router"; // MUST IMPORT FOR PASSING ID IN URL

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css']
})
export class QuestionComponent implements OnInit {

  constructor(private _LoginRegistrationService: LoginRegistrationService, private _Router: Router, _activatedRoute: ActivatedRoute) { }

  question = new Question();

  ngOnInit() { }

  submitquestion() {
      this.question.created_by = Cookie.get('logged_id');
      console.log(this.question)
      this._LoginRegistrationService.submitQuestion(this.question)
      .then((data) => {
          if(data.error) {
              alert(data.messages)
          } else {
              console.log("DATA Inside Question Component")
              console.log(data)
              this._Router.navigateByUrl('question')
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
