import { Router } from '@angular/router';
import { Job } from './models/job';
import { JwtService } from './../auth/jwt.service';
import { Injectable } from '@angular/core';
import { Observable } from "rxjs/Observable";
import { Http, Response, RequestOptions } from '@angular/http'
import { Headers } from '@angular/http';
import 'rxjs/add/operator/map'

@Injectable()
export class JobsService {
  public jobList: Job[];
  private apiUrl = 'http://ughjobs.jdsieci.eu/api/job'
  constructor(private http: Http,
    private authService: JwtService,
    private router: Router) { }

  getJob(id) {
    let headers = new Headers();
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.get(this.apiUrl+'/'+id, { headers: headers });
  }

  getJobs() {
    let headers = new Headers();
    let userList: Job[];
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.get(this.apiUrl, { headers: headers });
  }

  register(user) {
    let headers = new Headers();
    headers.append("Access-Control-Allow-Origin", "*");
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.post(this.apiUrl, {
      title: user.title,
      description: user.description,
    }, { headers: headers }).subscribe(data => {
      this.router.navigate(['/jobs']);
    });
  }

  apply(id) {
    let headers = new Headers();
    headers.append("Access-Control-Allow-Origin", "*");
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.post('http://localhost:5000/application', {
      job_id: id,
      comment: "Szybka Aplikacja"
    }, { headers: headers }).subscribe(data => {
      console.log(id);
    });
  }

  deleteJob(id) : Observable<any> {
    let headers = new Headers();
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.delete(this.apiUrl+'/'+id, { headers: headers });
  }
}
