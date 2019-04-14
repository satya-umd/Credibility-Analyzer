import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DemosComponent } from './demos.component';
import { DEMOS } from '../mock-demos';

describe('DemosComponent', () => {
  let component: DemosComponent;
  let fixture: ComponentFixture<DemosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DemosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DemosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
}

export class DemosComponent implements OnInit {
  demos = DEMOS;
}

);
