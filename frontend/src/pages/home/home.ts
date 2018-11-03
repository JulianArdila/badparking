import { Home2Page } from './../home2/home2';
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RegistroMalParquedoPage } from '../registro-mal-parquedo/registro-mal-parquedo';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  ingresar:any;
  Home2Page: any;

  constructor(public navCtrl: NavController) {
    this.Home2Page = Home2Page;
    this.ingresar = RegistroMalParquedoPage;
  }
  LogOut(){
    
  }

}
