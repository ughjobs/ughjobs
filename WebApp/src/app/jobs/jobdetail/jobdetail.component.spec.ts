import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { JobdetailComponent } from './jobdetail.component';

describe('JobdetailComponent', () => {
  let component: JobdetailComponent;
  let fixture: ComponentFixture<JobdetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ JobdetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(JobdetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
