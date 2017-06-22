import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ObsChildTwoComponent } from './obs-child-two.component';

describe('ObsChildTwoComponent', () => {
  let component: ObsChildTwoComponent;
  let fixture: ComponentFixture<ObsChildTwoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ObsChildTwoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ObsChildTwoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
