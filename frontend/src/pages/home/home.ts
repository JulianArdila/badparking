import { RestProvider } from './../../providers/rest/rest';
import { Home2Page } from './../home2/home2';
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RegistroMalParquedoPage } from '../registro-mal-parquedo/registro-mal-parquedo';
import { LoginPage } from '../login/login';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  ingresar:any;
  Home2Page: any;

  constructor(public navCtrl: NavController, public restProvider: RestProvider) {
    this.Home2Page = Home2Page;
    this.ingresar = RegistroMalParquedoPage;
  }
  
  logOut(){
    this.restProvider.logOut().then((result:any) => {
      console.log(result);
      localStorage.clear();
      this.navCtrl.setRoot(LoginPage);
    }, (err) => {
      console.log(err);
    });
  }

}
