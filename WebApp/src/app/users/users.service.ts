import { JwtService } from './../auth/jwt.service';
import { User } from './users-list/models/user';
import { Injectable } from '@angular/core';
import { Observable } from "rxjs/Observable";
import { Http, RequestOptions } from '@angular/http'
import { Headers, Response } from '@angular/http';
import 'rxjs/add/operator/map'
import { Router } from '@angular/router';

@Injectable()
export class UsersService {
  private apiUrl = 'http://ughjobs.jdsieci.eu/api/user';
  public userList : User[];
  constructor(private http : Http,
              private authService: JwtService,
            private router : Router) { }

  getUsers() {
    let headers = new Headers();
    let userList : User[] ;
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.get(this.apiUrl, {headers : headers });
  }

  getJob(id) {
    let headers = new Headers();
    let user: User[];
    let params = JSON.parse(localStorage.getItem("currentUser"))
    headers.append("x-access-token", params["token"]);
    return this.http.get(this.apiUrl+'/'+id, { headers: headers });
  
  }
    deleteUser(id) : Observable<any> {
      let headers = new Headers();
      let params = JSON.parse(localStorage.getItem("currentUser"))
      headers.append("x-access-token", params["token"]);
      return this.http.delete(this.apiUrl+'/'+id, { headers: headers });
    }
}
