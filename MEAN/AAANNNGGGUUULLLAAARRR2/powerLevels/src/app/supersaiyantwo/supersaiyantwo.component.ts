import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-supersaiyantwo',
  templateUrl: './supersaiyantwo.component.html',
  styleUrls: ['./supersaiyantwo.component.css']
})
export class SupersaiyantwoComponent implements OnInit {

  @Input() initialPowerLevel
  newPowerLevel: number;

  constructor() { }

  calculatePowerUp(){
    console.log('This function works!')
    this.newPowerLevel = this.initialPowerLevel * 150;
  }

  ngOnInit() {
    console.log(this.initialPowerLevel, 'Initial Power Level');
    this.calculatePowerUp();
  }

}
