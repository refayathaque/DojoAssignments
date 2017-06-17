import { Component, OnInit, Input} from '@angular/core';

@Component({
  selector: 'app-secondchild',
  templateUrl: './secondchild.component.html',
  styleUrls: ['./secondchild.component.css']
})
export class SecondchildComponent implements OnInit {

    @Input() objPassedDown;

  constructor() { }

  ngOnInit() {
  }

}
