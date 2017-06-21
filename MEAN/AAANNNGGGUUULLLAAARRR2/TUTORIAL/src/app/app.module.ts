import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // MANUALLY DO THIS FOR FORMS!
import { HttpModule } from '@angular/http'; // MANUALLY DO THIS FOR SERVICES!
import { AppRoutingModule } from './app-routing.module'; // MANUALLY DO THIS FOR ROUTING!
import { RouterModule, Routes } from '@angular/router'; // MANUALLY DO THIS FOR ROUTING!
import { AppComponent } from './app.component';
import { ChildComponent } from './child/child.component';
import { GrandchildComponent } from './child/grandchild/grandchild.component';
import { SecondchildComponent } from './secondchild/secondchild.component';
import { HttpService } from './http.service';
import { HomeComponent } from './home/home.component';
import { OfficeComponent } from './office/office.component';
import { TaskComponent } from './task/task.component';
import { CommunicateService } from './communicate.service';

@NgModule({
  declarations: [
    AppComponent,
    ChildComponent,
    GrandchildComponent,
    SecondchildComponent,
    HomeComponent,
    OfficeComponent,
    TaskComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, // MANUALLY DO THIS ROUTING!
    FormsModule, // MANUALLY DO THIS FOR FORMS!
    HttpModule // MANUALLY DO THIS FOR SERVICES!
  ],
  providers: [HttpService, CommunicateService], // MANUALLY DO THIS FOR SERVICES!
  bootstrap: [AppComponent]
})

export class AppModule { }
