import { JwtService } from './../auth/jwt.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Observable';
import { Http,Response,  RequestOptions  } from '@angular/http';
import { Injectable } from '@angular/core';
import { Applicant } from './applicants-list/models/applicant';
import 'rxjs/add/operator/map'
import { Headers } from '@angular/http';

@Injectable()
export class ApplicantsService {
    public applicantsList : Applicant[];
    public load : boolean;
    private apiUrl = 'http://localhost:5000/application'
    constructor(private http : Http,
        private authService: JwtService,
        private router : Router) { }

    getApplicants() : Observable<Response> {
        let headers = new Headers();
        let userList : Applicant[] ;
        let params = JSON.parse(localStorage.getItem("currentUser"))
        headers.append("x-access-token", params["token"]);
        return this.http.get(this.apiUrl, { headers : headers });
    }

    deleteApplication(id) : Observable<any> {
        let headers = new Headers();
        let params = JSON.parse(localStorage.getItem("currentUser"))
        headers.append("x-access-token", params["token"]);
        return this.http.delete(this.apiUrl+'/'+id, { headers: headers });
    }

}
