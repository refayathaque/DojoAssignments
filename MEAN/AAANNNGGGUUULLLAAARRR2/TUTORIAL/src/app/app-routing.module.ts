import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component'; // MANUALLY DO THIS FOR COMPONENTS TO ROUTE TO
import { OfficeComponent } from './office/office.component';
import { TaskComponent } from './task/task.component';

const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'office', component: OfficeComponent },
    { path: 'task/:id', component: TaskComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
