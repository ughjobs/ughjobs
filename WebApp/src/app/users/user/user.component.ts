import { User } from './../users-list/models/user';
import { UsersService } from './../users.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router/';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  private ready : boolean;
  private user : User;
  private id : number;
  constructor(private router: ActivatedRoute,
    private service: UsersService) { }

  ngOnInit() {
    this.getUser();
  }

  getUser() {
    this.router.params.subscribe(params => this.id = params['id'])
    this.service.getJob(this.id).subscribe(data => {
      this.user = data.json()['user'];
      this.ready = true;
    });
  }
}
