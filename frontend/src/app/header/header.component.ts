import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit,OnDestroy {
  isAuthenticated:boolean = false;
  private userSub: Subscription;
  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.userSub = this.authService.user.subscribe((user)=>{
      this.isAuthenticated =!user? false: true;
    })
  }
  ngOnDestroy(){
    this.userSub.unsubscribe();
  }
  onLogout(){
    this.authService.logout();
  }

}
