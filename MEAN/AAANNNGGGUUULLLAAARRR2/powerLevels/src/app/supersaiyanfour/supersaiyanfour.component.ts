import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-supersaiyanfour',
  templateUrl: './supersaiyanfour.component.html',
  styleUrls: ['./supersaiyanfour.component.css']
})
export class SupersaiyanfourComponent implements OnInit {

  @Input() initialPowerLevel
  newPowerLevel: number;

  constructor() { }

  calculatePowerUp(){
    console.log('This function works!')
    this.newPowerLevel = this.initialPowerLevel * 90;
  }

  ngOnInit() {
    console.log(this.initialPowerLevel, 'Initial Power Level');
    this.calculatePowerUp();
  }

}
