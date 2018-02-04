import { NgModule } from '@angular/core';
import { Route } from "@angular/router/src";
import { RouterModule } from '@angular/router';

const USERS_ROUTES : Route[] = [
    //{ path: 'users/:id', component: UserDetailsComponent }
];

@NgModule({
    imports: [ 
        RouterModule.forChild(USERS_ROUTES)
    ],

    exports : [
        RouterModule
    ]
})

export class UsersRoutingModule {}