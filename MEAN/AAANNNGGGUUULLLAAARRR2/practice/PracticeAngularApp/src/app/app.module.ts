import { BrowserModule } from '@angular/platform-browser';

import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { ComponentOneComponent } from './component-one/component-one.component';

import { FormsModule } from '@angular/forms'; // <-- Import FormsModule

import { HttpModule } from '@angular/http';

@NgModule({
  declarations: [
    AppComponent,
    ComponentOneComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
