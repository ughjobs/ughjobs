import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { JobComponent } from './job/job.component';
import { JobdetailComponent } from './jobdetail/jobdetail.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [JobComponent, JobdetailComponent]
})
export class JobsModule { }
