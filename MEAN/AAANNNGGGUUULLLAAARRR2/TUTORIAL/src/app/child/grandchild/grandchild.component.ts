import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-grandchild',
  templateUrl: './grandchild.component.html',
  styleUrls: ['./grandchild.component.css']
})
export class GrandchildComponent implements OnInit {

    @Output() eventSendingDataUp = new EventEmitter();

    object1 = {message: 'I am data being passed up from the grandchild (CHILD) component!'}

    functionSendingDataUp(){
        this.eventSendingDataUp.emit(this.object1);
    }

  constructor() { }

  ngOnInit() {
  }

}
