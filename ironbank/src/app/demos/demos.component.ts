import { Component, OnInit } from '@angular/core';
import {Demo} from '../demo';
import { DemoService } from '../demo.service';

@Component({
  selector: 'app-demos',
  templateUrl: './demos.component.html',
  styleUrls: ['./demos.component.css']
})
export class DemosComponent implements OnInit {
  demos: Demo[];

 constructor(private demoService: DemoService) { }
 
  ngOnInit() {
    this.getDemos();
  }

  getDemos(): void {
    this.demoService.getDemos()
        .subscribe(demos => this.demos = demos);
  }
}
