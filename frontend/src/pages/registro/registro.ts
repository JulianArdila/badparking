import { LoginPage } from './../login/login';
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
    this.restProvider.ConsultTipoUsuarios().then(data =>{this.tipoUsuario=data;console.log(this.tipoUsuario);})
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad RegistroPage');
    this.consultarTipoUsuarios();
  }

  Registrar(){
    var data = {'username':this.usuario,'password':this.clave,'nombre':this.nombre,'apellido':this.apellido,'telefono':this.telefono,'correo':this.correo,'fecha_nacimiento':this.fecha,'tipo':this.tipo};
    this.restProvider.registro(data).then((result:any) => {this.navCtrl.setRoot(LoginPage);},(err)=>{console.log(err);});
  }

}
