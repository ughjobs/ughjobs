import { Router } from '@angular/router';
import { User } from './../users/users-list/models/user';
import { RequestOptions} from '@angular/http';
import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map'
import { element } from 'protractor';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from "@angular/common/http";


@Injectable()
export class JwtService {

  private BASE_URL: string = 'http://ughjobs.jdsieci.eu/api';
  public username: string = "";
  public loggedIn: boolean = false
  constructor(private http: Http, private router: Router) { }
  login(user){
    let headers = new Headers();
    headers.append("Authorization", "Basic " + btoa(user.username +':'+user.password));
    headers.append("Content-Type", "application/json");
    let url: string = `${this.BASE_URL}/login`;
    return this.http.get(url,{headers : headers}).subscribe(data => {
      console.log(data);
      let token = data.json();
      localStorage.setItem('currentUser', JSON.stringify({token: token["token"], name: user.username }))
      this.username = user.username;
      this.router.navigate(['/']);
      this.loggedIn = true;
      console.log(this.username);
    });
  }

  register(user){
    let headers = new Headers();
    headers.append("Access-Control-Allow-Origin","*");
    let url: string = `${this.BASE_URL}/user`;
    return this.http.post(url,{
      login: user.login,
      password: user.password,
      name: user.name,
      surname: user.surname,
      city: user.city,
      street: user.street,
      street_number: user.street_number,
      apartment: user.apartment

    }, {headers : headers} ).subscribe(data => {    
    });
  }

  logout()
  {
    return localStorage.setItem("currentUser", null);
  }
}
        
        




