import { Observable } from 'rxjs/Observable';
import { Applicant } from './models/applicant';
import { ApplicantsService } from './../applicants.service';
import { Component, OnInit } from '@angular/core';
import { Response } from '@angular/http';

@Component({
  selector: 'app-applicants-list',
  templateUrl: './applicants-list.component.html',
  styleUrls: ['./applicants-list.component.css']
})
export class ApplicantsListComponent implements OnInit {

  applicants: Applicant[] = [];
  constructor(private applicantService: ApplicantsService) {
  }

  ngOnInit() {
    this.loadApplications()
  }

  loadApplications() {
    this.applicants = this.applicantService.applicantsList;
    this.applicantService.getApplicants().subscribe(data => {
      let dane = (data.json());
      console.log(dane);
      this.applicants = dane["applications"];
    });
  }
  deleteApplication(id) {
    this.applicantService.deleteApplication(id).subscribe(()=>
    this.loadApplications())
  }
}
