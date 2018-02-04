import { UserComponent } from './users/user/user.component';
import { JobComponent } from './jobs/job/job.component';
import { ApplicantsService } from './applicants/applicants.service';
import { JobRoutingModule } from './jobs/jobs-routing.module';
import { UsersRoutingModule } from './users/users-routing.module';
import { AppRoutingModule } from './app-routing.module';
import { CoreModule } from './core-module/core-module.module';
import { UsersModule } from './users/users.module';
import { UsersService } from './users/users.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { UsersListComponent } from './users/users-list/users-list.component';
import { JobsListComponent } from './jobs/jobs-list/jobs-list.component';
import {RouterModule} from '@angular/router';
import { ApplicantsListComponent } from './applicants/applicants-list/applicants-list.component';
import { SigninComponent } from './auth/signin/signin.component';
import { SignupComponent } from './auth/signup/signup.component'
import { FormsModule } from "@angular/forms";
import { ReactiveFormsModule } from "@angular/forms";
import { JwtService } from './auth/jwt.service';
import { HttpModule } from '@angular/http'
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { MainComponent } from './main/main.component';
import { JobsService } from './jobs/jobs.service';
import { JobdetailComponent } from './jobs/jobdetail/jobdetail.component';


@NgModule({
  declarations: [
    AppComponent,
    JobsListComponent,
    ApplicantsListComponent,
    SigninComponent,
    SignupComponent,
    MainComponent,
    JobComponent,
    JobdetailComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,                          
    ReactiveFormsModule,   
    HttpModule,
    UsersModule,
    CoreModule,
    AppRoutingModule,
    UsersRoutingModule,
    JobRoutingModule,
    HttpModule,
    HttpClientModule,
  ],
  providers: [UsersService, JwtService, ApplicantsService, JobsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
