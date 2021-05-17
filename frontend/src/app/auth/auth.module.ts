import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { AuthComponent } from './auth.component';
import { AuthService } from './auth.service';

@NgModule({
    declarations:[
        AuthComponent
    ],
    imports: [
        ReactiveFormsModule,
        CommonModule
    ],
    providers: [AuthService]
})
export class AuthModule{}