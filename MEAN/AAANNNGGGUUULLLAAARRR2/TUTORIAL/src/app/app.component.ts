import { Component, OnDestroy } from '@angular/core';
import { User } from './user'; // MUST IMPORT CONSTRUCTOR CLASSES
import { HttpService } from './http.service'; // MUST BE DONE MANUALLY FOR SERVICES
import { BehaviorSubject } from 'rxjs/BehaviorSubject'; // MUST BE DONE MANUALLY FOR SERVICES WITH OBSERVABLES
import { CommunicateService } from './communicate.service'; // MUST BE DONE MANUALLY FOR SERVICES
import { Subscription } from 'rxjs/Subscription'; // MANUALLY DO THIS WHEN USING OBSERVABLES AND SUBSCRIPTIONS

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    title: string = 'Angular 2 Tutorial';
    x: number = 10;
    y: number = 5;
    users = [
        {firstname: 'Refayat', lastname: 'Haque'},
        {firstname: 'Ishaba', lastname: 'Haque'}
    ];
    numbers = [1, 2, 3, 4];
    today = Date.now();
    fontcolor = 'blue';
    switchon: boolean = true;
    switchoff: boolean = false;
    increaseXBy10(){
        this.x += 10; // MUST REFERENCE VARIABLES INSIDE CLASS WITH 'THIS'!
    }
    increaseYBy10(){
        this.y += 10;
    }

    personWithEmail = {email: ""};
    emails = [];
    emailSubmission(){
        this.emails.push(this.personWithEmail)
        console.log(this.personWithEmail)
        this.personWithEmail = {email: ""}
    }

    user = new User();
    usersarray = [];
    registrationFormSubmission() {
        console.log(this.user)
        this.usersarray.push(this.user);
        this.user = new User();
    }

    object = {message: 'This is the object we are passing down from PARENT to CHILD'}
    refayatGitHubInfo = [];

    getRefayatGitHubInfo(){
        this._httpService.retrieveGitHubInfo()
        .then( refayatGitHubInfo => { this.refayatGitHubInfo = refayatGitHubInfo }) // .then is a CALLBACK method
        .catch( err => { console.log(err); })
    }

    //
    constructor(private _httpService: HttpService, private _communicateService: CommunicateService){
        _communicateService.updateCars(this.cars);
        _communicateService.observedCars.subscribe(
            cars => this.cars = cars,
            (err) => {},
            () => {}
        );
    } // DEPENDENCY INJECTION! Using HttpService from class exported above from http.service.ts
    // The constructor function is like ONINIT, it registers services, and runs whatever functions are inside of it, once the page loads. We can pass in all our services inside of it. The constructor function is used for DEPENDENCY INJECTION!

    subscription: Subscription;

    cars = [{model:'Toyota Camry'}, {model:'Honda Accord'}];

    changeData(){
        this.cars = [{model:'Toyota Camry'}, {model:'Honda Accord'}];
        this._communicateService.updateCars(this.cars);
    }
    //

}
