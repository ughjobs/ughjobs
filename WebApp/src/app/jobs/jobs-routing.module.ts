import { NgModule } from '@angular/core';
import { Route } from "@angular/router/src";
import { RouterModule } from '@angular/router';

const JOB_ROUTES : Route[] = [
    //{path: 'jobs/:id', component: JobDetailsComponent}
];

@NgModule({
    imports: [ 
        RouterModule.forRoot(JOB_ROUTES)
    ],

    exports : [
        RouterModule
    ]
})

export class JobRoutingModule {}