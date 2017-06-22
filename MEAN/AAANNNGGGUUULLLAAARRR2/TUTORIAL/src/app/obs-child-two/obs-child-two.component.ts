import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router'; // MANUALLY DO THIS FOR ROUTES WITH PARAMETERS
import { OnDestroy } from '@angular/core'; // MANUALLY DO THIS WHEN USING OBSERVABLES AND SUBSCRIPTIONS
import { Subscription } from 'rxjs/Subscription'; // MANUALLY DO THIS WHEN USING OBSERVABLES AND SUBSCRIPTIONS
import { CommunicateService } from '../communicate.service'; // MUST BE DONE MANUALLY FOR SERVICES
import { BehaviorSubject } from 'rxjs/BehaviorSubject'; // MUST BE DONE MANUALLY FOR SERVICES WITH OBSERVABLES

@Component({
  selector: 'app-obs-child-two',
  templateUrl: './obs-child-two.component.html',
  styleUrls: ['./obs-child-two.component.css']
})
export class ObsChildTwoComponent implements OnInit {

    subscription: Subscription;
    cars = [];

  constructor(private _communicateService: CommunicateService) {
      this.subscription = this._communicateService.observedCars.subscribe(
          (cars) => this.cars = cars,
          (err) => {},
          () => {}
      );
      console.log(this._communicateService.observedCars.getValue());
  }

  changeData(){
      this.cars = [{model:'Toyota Rav4'}, {model:'Honda CR-V'}];
      this._communicateService.updateCars(this.cars);
      console.log(this._communicateService.observedCars.getValue());
  }

  ngOnDestroy() {
      this.subscription.unsubscribe();
  }

  ngOnInit() {
  }

}
