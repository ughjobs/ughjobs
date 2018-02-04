import { User } from './../../users/users-list/models/user';
import { JwtService } from './../jwt.service';
import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";

@Component({
  moduleId: module.id,
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

 data = {};


  constructor(
      private router: Router,
      private authenticationService: JwtService) { }

  ngOnInit() {
    
  }

  login() {
      this.authenticationService.login(this.data)
  }
}

