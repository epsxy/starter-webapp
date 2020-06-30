import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WorksListComponent } from './ui/works/works-list.component';

const routes: Routes = [{ path: 'works', component: WorksListComponent }];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
