import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-saiyan',
  templateUrl: './saiyan.component.html',
  styleUrls: ['./saiyan.component.css']
})
export class SaiyanComponent implements OnInit {

  @Input() initialPowerLevel
  newPowerLevel: number;

  constructor() { }

  calculatePowerUp(){
    console.log('This function works!')
    this.newPowerLevel = this.initialPowerLevel * 10;
  }

  ngOnInit() {
    console.log(this.initialPowerLevel, 'Initial Power Level');
    this.calculatePowerUp();
  }

}
