import { Component } from '@angular/core';

@Component({
    selector: 'app-works-list',
    templateUrl: 'works-list.component.html',
    styleUrls: ['works-list.component.sass'],
})
export class WorksListComponent {
    works = [
        { id: 1, name: 'My First Work', description: 'lorem ipsum', progress: 30 },
        { id: 2, name: 'My Second Work', description: 'lorem ipsum', progress: 80 },
        { id: 3, name: 'My Third Work', description: 'lorem ipsum', progress: 20 },
        { id: 4, name: 'My Fourth Work', description: 'lorem ipsum', progress: 95 },
    ];
    isCreatingNewWork = false;

    constructor() {}

    createWork(): void {
        this.isCreatingNewWork = true;
    }

    onCreateWorkCancel(): void {
        this.isCreatingNewWork = false;
    }
}
