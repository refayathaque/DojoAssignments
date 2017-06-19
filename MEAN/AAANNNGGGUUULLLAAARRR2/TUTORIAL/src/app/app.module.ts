import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // MANUALLY DO THIS FOR FORMS!
import { HttpModule } from '@angular/http'; // MANUALLY DO THIS FOR SERVICES!

import { AppComponent } from './app.component';
import { ChildComponent } from './child/child.component';
import { GrandchildComponent } from './child/grandchild/grandchild.component';
import { SecondchildComponent } from './secondchild/secondchild.component';
import { HttpService } from './http.service'; // MANUALLY DO THIS FOR SERVICES!

@NgModule({
  declarations: [
    AppComponent,
    ChildComponent,
    GrandchildComponent,
    SecondchildComponent
  ],
  imports: [
    BrowserModule,
    FormsModule, // MANUALLY DO THIS FOR FORMS!
    HttpModule // MANUALLY DO THIS FOR SERVICES!
  ],
  providers: [HttpService], // MANUALLY DO THIS FOR SERVICES!
  bootstrap: [AppComponent]
})
export class AppModule { }
