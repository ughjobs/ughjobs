import { UserComponent } from './users/user/user.component';
import { JobdetailComponent } from './jobs/jobdetail/jobdetail.component';
import { JobComponent } from './jobs/job/job.component';
import { ApplicantsListComponent } from './applicants/applicants-list/applicants-list.component';
import { MainComponent } from './main/main.component';
import { SignupComponent } from './auth/signup/signup.component';
import { SigninComponent } from './auth/signin/signin.component';
import { JobsListComponent } from './jobs/jobs-list/jobs-list.component';
import { UsersListComponent } from './users/users-list/users-list.component';
import { NgModule } from '@angular/core';
import { Route } from "@angular/router/src";
import { RouterModule } from '@angular/router';

const APP_ROUTES : Route[] = [
    {path: 'users', component: UsersListComponent},
    {path: 'jobs', component: JobsListComponent},
    {path: 'signup', component: SignupComponent},
    {path: 'signin', component: SigninComponent},
    {path: '', component: MainComponent},
    {path: 'applications', component: ApplicantsListComponent},
    {path: 'job', component: JobComponent},
    {path: 'jobdetails/:id', component: JobdetailComponent},
    {path: 'user/:id', component: UserComponent},

];

@NgModule({
    imports: [ 
        RouterModule.forRoot(APP_ROUTES)
    ],

    exports : [
        RouterModule
    ]
})

export class AppRoutingModule {}