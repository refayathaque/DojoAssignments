import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router'; // MANUALLY DO THIS FOR ROUTES WITH PARAMETERS
import { OnDestroy } from '@angular/core'; // MANUALLY DO THIS WHEN USING OBSERVABLES AND SUBSCRIPTIONS
import { Subscription } from 'rxjs/Subscription'; // MANUALLY DO THIS WHEN USING OBSERVABLES AND SUBSCRIPTIONS

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

    subscription: Subscription; // declaring variable 'subscription' to TYPE SUBSCRIPTION

    identification = [];

    constructor(private _route: ActivatedRoute) {
        this.subscription = this._route.params.subscribe((param)=>{
            console.log("TaskComponent loaded and url id given is: ", param.id); // OBSERVABLE!
            this.identification.push(param.id);
        })
    }

    ngOnDestroy(){ // requires 'onDestroy' import
  	    this.subscription.unsubscribe(); // requires declaring variable 'subscription' to TYPE SUBSCRIPTION, and having variable 'subscription' be ASSIGNED to the OBSERVABLE
    }

  ngOnInit() {
  }

}
