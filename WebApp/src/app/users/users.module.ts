import { UsersListComponent } from './users-list/users-list.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserComponent } from './user/user.component';

@NgModule({
  imports: [
    CommonModule
  ],
  exports: [UsersListComponent],
  declarations: [UsersListComponent, UserComponent]
})
export class UsersModule { }
