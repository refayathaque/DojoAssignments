import { Injectable } from '@angular/core';
import { Http } from '@angular/http'; // MUST BE MANUALLY INSERTED!
import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map';

@Injectable()
export class HttpService {

    constructor(private _http: Http) { }
    retrieveTasks() {
      return this._http.get('/tasks').map(data=>data.json()).toPromise()
    }

}
