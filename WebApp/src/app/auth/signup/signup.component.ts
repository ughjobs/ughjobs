import { Router } from '@angular/router';
import { JwtService } from './../jwt.service';
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  data = {}

  constructor(private router: Router,
    private authenticationService: JwtService) { }

  ngOnInit() {
  }

  register() {
    this.authenticationService.register(this.data)
} 
}
