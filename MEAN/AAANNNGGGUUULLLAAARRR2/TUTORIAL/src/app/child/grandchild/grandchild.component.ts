import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-grandchild',
  templateUrl: './grandchild.component.html',
  styleUrls: ['./grandchild.component.css']
})
export class GrandchildComponent implements OnInit {

    @Output() functionSendingDataUp = new EventEmitter();

    object1 = {message: 'I am data being passed up from the grandchild (CHILD) component!'}

    eventSendingDataUp(){
        this.functionSendingDataUp.emit(this.object1);
    }

  constructor() { }

  ngOnInit() {
  }

}
