import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component'; // MANUALLY DO THIS FOR COMPONENTS TO ROUTE TO
import { OfficeComponent } from './office/office.component';
import { TaskComponent } from './task/task.component';
import { ObsChildOneComponent } from './obs-child-one/obs-child-one.component';
import { ObsChildTwoComponent } from './obs-child-two/obs-child-two.component';
import { GrandchildComponent } from './child/grandchild/grandchild.component';
import { ChildComponent } from './child/child.component';

const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'office', component: OfficeComponent },
    { path: 'task/:id', component: TaskComponent },
    { path: 'obs-child-one', component: ObsChildOneComponent },
    { path: 'obs-child-two', component: ObsChildTwoComponent },
    { path: 'child', component: ChildComponent, children:[
		{ path: 'grandchild', component: GrandchildComponent }
    ]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
