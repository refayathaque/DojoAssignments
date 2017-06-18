import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { ChildComponent } from './child/child.component';
import { GrandchildComponent } from './child/grandchild/grandchild.component';
import { SecondchildComponent } from './secondchild/secondchild.component';
import { HttpService } from './http.service'; // MUST BE DONE MANUALLY FOR SERVICES

@NgModule({
  declarations: [
    AppComponent,
    ChildComponent,
    GrandchildComponent,
    SecondchildComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [HttpService], // MUST BE DONE MANUALLY FOR SERVICES
  bootstrap: [AppComponent]
})
export class AppModule { }
