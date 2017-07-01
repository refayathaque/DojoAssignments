import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserbucketlistComponent } from './userbucketlist.component';

describe('UserbucketlistComponent', () => {
  let component: UserbucketlistComponent;
  let fixture: ComponentFixture<UserbucketlistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserbucketlistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserbucketlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
