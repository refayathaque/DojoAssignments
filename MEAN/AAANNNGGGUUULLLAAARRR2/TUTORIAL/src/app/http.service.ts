import { Injectable } from '@angular/core';
import { Http } from '@angular/http'; // MUST BE MANUALLY INSERTED!

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class HttpService {

    constructor(private _http: Http) { } // Using Http from angular module imported from above
    retrieveTasks() {
      return this._http.get('https://api.github.com/users/refayathaque').map(data=>data.json()).toPromise()
    }

}
