import { Component, OnInit } from '@angular/core';
import { Cookie } from "ng2-cookies";
import { Router } from "@angular/router";
import { LoginRegistrationService } from "app/loginregistration.service";
import { Answer } from '../answer'; // MUST IMPORT CONSTRUCTOR CLASSES
import { ActivatedRoute } from "@angular/router"; // MUST IMPORT FOR PASSING ID IN URL

@Component({
  selector: 'app-answer',
  templateUrl: './answer.component.html',
  styleUrls: ['./answer.component.css']
})
export class AnswerComponent implements OnInit {

  constructor(private _LoginRegistrationService: LoginRegistrationService, private _Router: Router, _activatedRoute: ActivatedRoute) { } // Dependency Injections for some IMPORTS

  answer = new Answer(); // Instantiating class 'question'

  ngOnInit() { }

  submitanswer() {
      this.answer.created_by = Cookie.get('logged_id');
      console.log('Answer Component Before Service Call', this.answer)
      this._LoginRegistrationService.submitAnswer(this.answer)
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

}
