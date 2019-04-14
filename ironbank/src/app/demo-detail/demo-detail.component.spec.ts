import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DemoDetailComponent } from './demo-detail.component';

describe('DemoDetailComponent', () => {
  let component: DemoDetailComponent;
  let fixture: ComponentFixture<DemoDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DemoDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DemoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
