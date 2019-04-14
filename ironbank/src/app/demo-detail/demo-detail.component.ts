import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { DemoService }  from '../demo.service';
import { Component, OnInit } from '@angular/core';
import { Demo } from '../demo';
@Component({
  selector: 'app-demo-detail',
  templateUrl: './demo-detail.component.html',
  styleUrls: ['./demo-detail.component.css']
})
export class DemoDetailComponent implements OnInit {
	demo: Demo;
	constructor(
        private route: ActivatedRoute,
        private demoService: DemoService,
        private location: Location
      ) {}
	

  ngOnInit(): void {
    this.getDemo();
  }

  getDemo(): void{
    const id = +this.route.snapshot.paramMap.get('id');
    this.demoService.getDemo(id)
      .subscribe(demo => this.demo = demo);
  }
 
  goBack(): void {
    this.location.back();
  }

}
