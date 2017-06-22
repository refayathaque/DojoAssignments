import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject'; // MANUALLY DO THIS! (THIS IS A TYPE OF SUBJECT, WHICH IS A TYPE OF OBSERVABLE)

@Injectable()
export class CommunicateService {

    observedCars = new BehaviorSubject(null);

    // 'observedCars' is the actual OBSERVABLE

    // Any component can call this SERVICE and the METHOD inside this service and pass in an ARRAY of cars. At the point we are calling on our OBSERVABLE, and calling NEXT to pass in the cars. By doing this we are changing the value of the 'observedCars' OBSERVABLE. When we do this anything that is SUBSCRIBED to this OBSERVABLE will be INVOKED and it will TRIGGER a CALLBACK and it can update itself. When we call the service we can also RETRIEVE the OBSERVABLE.

    updateCars(cars: Array<any>) {
        this.observedCars.next(cars);
    }

  constructor() { }

}
