import { Component, OnInit } from '@angular/core';
import { Demo } from '../demo';
import { DemoService } from '../demo.service';
 
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: [ './dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {
  demos: Demo[] = [];
 
  constructor(private demoService: DemoService) { }
 
  ngOnInit() {
    this.getDemos();
  }
 
  getDemos(): void {
    this.demoService.getDemos()
      .subscribe(demos => this.demos = demos);
  }
}