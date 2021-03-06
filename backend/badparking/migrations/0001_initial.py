# Generated by Django 2.1 on 2018-10-29 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IngreMalParqueado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_ubicacion', models.CharField(max_length=300)),
                ('latitud', models.CharField(max_length=60)),
                ('longitud', models.CharField(max_length=60)),
                ('fecha_de_registro', models.DateField()),
                ('hora_de_registro', models.TimeField()),
                ('placa', models.CharField(max_length=20)),
                ('confiden', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField(auto_now_add=True)),
                ('correo', models.CharField(max_length=150)),
                ('telefono', models.IntegerField()),
                ('usuario', models.CharField(max_length=60)),
                ('clave', models.CharField(max_length=60)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badparking.TipoUsuario')),
            ],
        ),
        migrations.AddField(
            model_name='ingremalparqueado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badparking.Usuarios'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='ingreso_mal_parqueado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badparking.IngreMalParqueado'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badparking.Usuarios'),
        ),
    ]
