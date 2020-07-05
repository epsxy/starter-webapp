import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WorksListComponent } from './ui/works/works-list.component';
import { CommonModule } from '@angular/common';

const routes: Routes = [{ path: 'works', component: WorksListComponent }];

@NgModule({
    imports: [RouterModule.forRoot(routes), CommonModule],
    exports: [RouterModule],
})
export class AppRoutingModule {}
