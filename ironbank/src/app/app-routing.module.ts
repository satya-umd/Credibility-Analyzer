import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DemosComponent } from './demos/demos.component';
import { DashboardComponent }   from './dashboard/dashboard.component';
import { DemoDetailComponent }  from './demo-detail/demo-detail.component';
const routes: Routes = [
	{ path: '', redirectTo: '/dashboard', pathMatch: 'full' },
	{ path: 'demos', component: DemosComponent },
	{ path: 'dashboard', component: DashboardComponent },
	{ path: 'detail/:id', component: DemoDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
