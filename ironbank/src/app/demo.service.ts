import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';
 
import { Demo } from './demo';
import { DEMOS } from './mock-demos';
import { MessageService } from './message.service';
@Injectable({
  providedIn: 'root',
})
export class DemoService {

  constructor(private messageService: MessageService) { } 
  getDemos(): Observable<Demo[]>{
  	//this.messageService.add('DemoService: fetched Demos');
  	return of(DEMOS);
  }
  getDemo(id: number): Observable<Demo> {
    // TODO: send the message _after_ fetching the hero
    //this.messageService.add(`DemoService: fetched hero id=${id}`);
    return of(DEMOS.find(demo => demo.id === id));
  }
}
