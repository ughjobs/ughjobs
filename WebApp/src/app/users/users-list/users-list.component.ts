import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { UsersService } from '../users.service';
import { User } from './models/user';


@Component({
  selector: 'app-users-list',
  templateUrl: './users-list.component.html',
  styleUrls: ['./users-list.component.css']
})
export class UsersListComponent implements OnInit {
  users: User[];
  constructor(private usersService: UsersService,
  private router : Router) { }

  ngOnInit() {
    this.getUsers();
  }

  getUser(id)
  {
    this.router.navigate(['/user/'+id]);
  }

  getUsers()
  {
    this.usersService.getUsers().subscribe(data => {
      let dane = (data.json());
      this.users = dane["users"];
    });
  }

  deleteUser(id)
  {
    this.usersService.deleteUser(id).subscribe(()=> this.getUsers())
  }
}
