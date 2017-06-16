import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-supersaiyan',
  templateUrl: './supersaiyan.component.html',
  styleUrls: ['./supersaiyan.component.css']
})
export class SupersaiyanComponent implements OnInit {

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
