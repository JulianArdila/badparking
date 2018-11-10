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
  usuario:Number;
  datosUsuarios:any;
  constructor(public navCtrl: NavController, public restProvider: RestProvider) {
    if(window.localStorage['tipo']==1){
      this.Home2Page = Home2Page;
      this.ingresar = RegistroMalParquedoPage;
    }else{
      this.Home2Page = Home2Page;
      this.ingresar = RegistroMalParquedoPage;
    }
    
  }
  ionViewDidLoad() {
    this.consultarUsuarioActual();
    }
  consultarUsuarioActual() {
    this.restProvider.getUsuarioActual()
    .then((data:any) => {
    this.usuario = data.tipo;
    window.localStorage['tipo']=this.usuario
    console.log(this.usuario)
    });
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
