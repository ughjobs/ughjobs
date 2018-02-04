import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApplicantsListComponent } from './applicants-list/applicants-list.component';

@NgModule({
  imports: [
    CommonModule
  ],
  exports: [ApplicantsListComponent],
  declarations: [ApplicantsListComponent]
})
export class ApplicantsModule { }
