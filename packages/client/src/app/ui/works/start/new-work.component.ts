import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
    selector: 'app-new-work',
    templateUrl: 'new-work.component.html',
    styleUrls: ['new-work.component.sass'],
})
export class NewWorkComponent {
    value = '';
    types = [{ name: 'Dummy', value: 'dummy' }];

    @Input('enable') enable = false;
    @Output() cancelEvent = new EventEmitter();

    constructor() {}

    onCancel(): void {
        this.cancelEvent.emit();
    }
}
