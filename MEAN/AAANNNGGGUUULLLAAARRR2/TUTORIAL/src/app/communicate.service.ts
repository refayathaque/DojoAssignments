import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject'; // MANUALLY DO THIS! (THIS IS A TYPE OF SUBJECT, WHICH IS A TYPE OF OBSERVABLE)

@Injectable()
export class CommunicateService {

    observedCars = new BehaviorSubject(null);
    updateCars(cars: Array<any>) {
        this.observedCars.next(cars);
    }

  constructor() { }

}
