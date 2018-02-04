import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { JwtService } from '../../auth/jwt.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
  
})
export class SidebarComponent implements OnInit {

  constructor( private authenticationService: JwtService, private router : Router) { }

  ngOnInit() {
    if(localStorage.getItem("currentUser") != "null")
    {

    }
  }

  isLoggedIn()
  {
    if(localStorage.getItem("currentUser") != "null")
      return true;
    else
      return false;
  }


  logout(){
    this.authenticationService.logout()
    this.router.navigate(['/']);
  }
}
