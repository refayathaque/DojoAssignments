import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ObsChildOneComponent } from './obs-child-one.component';

describe('ObsChildOneComponent', () => {
  let component: ObsChildOneComponent;
  let fixture: ComponentFixture<ObsChildOneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ObsChildOneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ObsChildOneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
