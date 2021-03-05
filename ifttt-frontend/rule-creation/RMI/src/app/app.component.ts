import { Component } from '@angular/core';
import { UserDataService } from './user-data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
//selector 对应静态html文件的路由选择
export class AppComponent {
  constructor(public userDataService: UserDataService) {}
  title = 'app';
}
