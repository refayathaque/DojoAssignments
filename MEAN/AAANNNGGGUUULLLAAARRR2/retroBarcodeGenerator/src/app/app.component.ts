import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Retro Barcode Generator';
  colors = ['BlanchedAlmond', 'Brown', 'CadetBlue', 'AliceBlue', 'Cyan', 'DarkGreen', 'Crimson', 'Coral', 'Gold', 'Green', 'HotPink', 'DimGray', 'Fuchsia', 'MediumVioletRed', 'MistyRose', 'Plum', 'Salmon']
  a: number = (Math.floor(Math.random() * 15)) + 0;
  b: number = (Math.floor(Math.random() * 15)) + 0;
  c: number = (Math.floor(Math.random() * 15)) + 0;
  d: number = (Math.floor(Math.random() * 15)) + 0;
  e: number = (Math.floor(Math.random() * 15)) + 0;
  f: number = (Math.floor(Math.random() * 15)) + 0;
}
