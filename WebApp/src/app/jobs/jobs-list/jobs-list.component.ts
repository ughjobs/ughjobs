import { Router } from '@angular/router';
import { JobsService } from './../jobs.service';
import { Component, OnInit } from '@angular/core';
import { Job } from '../models/job';

@Component({
  selector: 'app-jobs',
  templateUrl: './jobs-list.component.html',
  styleUrls: ['./jobs-list.component.css']
})
export class JobsListComponent implements OnInit {
  jobs: Job[];
  constructor(private jobsService: JobsService,
    private router: Router) { }

  ngOnInit() {
    this.loadJobs();
  }

  loadJobs() {
    this.jobsService.getJobs().subscribe(data => {
      let dane = (data.json());
      console.log(dane);
      this.jobs = dane["jobs"];
    });
  }
  apply(id) {
    this.jobsService.apply(id);
  }

  getJob(id) {
    this.router.navigate(['/jobdetails/' + id]);
  }

  delete(id) {
    this.jobsService.deleteJob(id).subscribe(data => {
      console.log("Usunięto pracę o ID" +id);
      this.loadJobs();
    });
  }
}