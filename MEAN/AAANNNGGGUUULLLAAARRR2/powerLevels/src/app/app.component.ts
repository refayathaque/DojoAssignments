import { Component, ViewChild } from '@angular/core';
import { SaiyanComponent } from './saiyan/saiyan.component';
import { SupersaiyanComponent } from './supersaiyan/supersaiyan.component';
import { SupersaiyantwoComponent } from './supersaiyantwo/supersaiyantwo.component';
import { SupersaiyanthreeComponent } from './supersaiyanthree/supersaiyanthree.component';
import { SupersaiyanfourComponent } from './supersaiyanfour/supersaiyanfour.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  @ViewChild(SaiyanComponent)
  private child: SaiyanComponent;
  @ViewChild(SupersaiyanComponent)
  private child1: SupersaiyanComponent;
  @ViewChild(SupersaiyantwoComponent)
  private child2: SupersaiyantwoComponent;
  @ViewChild(SupersaiyanthreeComponent)
  private child3: SupersaiyanthreeComponent;
  @ViewChild(SupersaiyanfourComponent)
  private child4: SupersaiyanfourComponent;
  title = 'Power';
  user = { initialPowerLevel: 0 }
  users: number[] = [];
  onSubmit(){
    console.log('Submitted', this.user.initialPowerLevel)
    if(this.users.length == 0){
      this.users.push(this.user.initialPowerLevel)
    }
    else{
      this.users = []
      this.users.push(this.user.initialPowerLevel)
    };
    console.log(typeof(this.users[0]))
    console.log(this.users[0])
    this.child.calculatePowerUp();
    this.child1.calculatePowerUp();
    this.child2.calculatePowerUp();
    this.child3.calculatePowerUp();
    this.child4.calculatePowerUp();
  }
}
