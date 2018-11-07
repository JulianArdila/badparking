import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';
import { ActionSheetController } from 'ionic-angular';
/**
 * Generated class for the RegistroPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-registro',
  templateUrl: 'registro.html',
})
export class RegistroPage {
  nombre: any;
  apellido:any;
  correo:any;
  tipo:any;
  clave:any;
  usuario:any;
  telefono:any;
  fecha:any;
  constructor(public navCtrl: NavController, public navParams: NavParams,public restProvider: RestProvider,public actionSheetCtrl: ActionSheetController) {

  }
  tipoUsuario:any;
  consultarTipoUsuarios(){
    this.restProvider.ConsultTipoUsuarios().then(data =>{this.tipoUsuario=data;})
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad RegistroPage');
  }

}
