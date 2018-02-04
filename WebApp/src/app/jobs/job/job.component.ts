import { JobsService } from './../jobs.service';
import { JwtService } from './../../auth/jwt.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-job',
  templateUrl: './job.component.html',
  styleUrls: ['./job.component.css']
})
export class JobComponent implements OnInit {

  data = {}
  
    constructor(private router: Router,
      private service: JobsService) { }
  
    ngOnInit() {
    }
  
    register() {
      this.service.register(this.data)
  } 
}
