import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { WorksModule } from './ui/works/works.module';
import { MatIconModule } from '@angular/material/icon';

@NgModule({
    declarations: [AppComponent],
    imports: [BrowserModule, AppRoutingModule, BrowserAnimationsModule, WorksModule, MatIconModule],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
