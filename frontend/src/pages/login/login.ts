import { HomePage } from './../home/home';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ActionSheetController } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';
import { Home2Page } from '../home2/home2';
import { empty } from 'rxjs/Observer';
import { RegistroPage } from '../registro/registro';
/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {
  usuario: any;
  clave: any;
  constructor(public navCtrl: NavController, public navParams: NavParams,public restProvider: RestProvider,public actionSheetCtrl: ActionSheetController) {
    if(window.localStorage['token']){
      this.navCtrl.setRoot(HomePage);
    }
  }
  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }
  logiIn() {
    var data = { 'username': this.usuario, 'password': this.clave };
    this.restProvider.login(data).then((result:any) => {
      console.log(result);
      window.localStorage['token'] = result.key;
      this.navCtrl.setRoot(HomePage);
    }, (err) => {
      console.log(err);
    });
  }
  mostrarRegistro() {
    this.navCtrl.push(RegistroPage);
    }
  
  presentActionSheet() {
    const actionSheet = this.actionSheetCtrl.create({
      title: 'Modify your album',
      buttons: [
        {
          text: 'Destructive',
          role: 'destructive',
          handler: () => {
            console.log('Destructive clicked');
          }
        },{
          text: 'Archive',
          handler: () => {
            console.log('Archive clicked');
          }
        },{
          text: 'Cancel',
          role: 'cancel',
          handler: () => {
            console.log('Cancel clicked');
          }
        }
      ]
    });
    actionSheet.present();
  }
}
