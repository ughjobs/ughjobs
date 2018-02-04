import { Job } from './../models/job';
import { Route, ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { JobsService } from '../jobs.service';


@Component({
  selector: 'app-jobdetail',
  templateUrl: './jobdetail.component.html',
  styleUrls: ['./jobdetail.component.css']
})
export class JobdetailComponent implements OnInit {
  private id : number;
  private job: Job;
  private ready : boolean;
  constructor(private jobserwis:JobsService,
  private route : ActivatedRoute) { }

  ngOnInit() {
    this.getJob();
  }

  getJob()
  {
    this.route.params.subscribe(params => this.id = params['id'] )
    this.jobserwis.getJob(this.id).subscribe(data => {
      this.job = data.json()['job'];
      this.ready = true;
  });
  }
}
