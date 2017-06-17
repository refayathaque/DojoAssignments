import { Component } from '@angular/core';
import { User } from './user'; // MUST IMPORT CONSTRUCTOR CLASSES!

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
}
