import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-supersaiyanthree',
  templateUrl: './supersaiyanthree.component.html',
  styleUrls: ['./supersaiyanthree.component.css']
})
export class SupersaiyanthreeComponent implements OnInit {

  @Input() initialPowerLevel
  newPowerLevel: number;

  constructor() { }

  calculatePowerUp(){
    console.log('This function works!')
    this.newPowerLevel = this.initialPowerLevel * 250;
  }

  ngOnInit() {
    console.log(this.initialPowerLevel, 'Initial Power Level');
    this.calculatePowerUp();
  }

}
