# Generated by Django 2.2.2 on 2019-11-27 17:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('introduccion', models.CharField(max_length=200)),
                ('resumen', models.CharField(max_length=200)),
                ('avance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('estado', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subtema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('contenido', models.CharField(max_length=200)),
                ('id_ova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_OVA.Objeto')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.CharField(max_length=200, null=True)),
                ('contenido', models.CharField(max_length=200)),
                ('id_Subtema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_OVA.Subtema')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaPregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=200)),
                ('id_Pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_OVA.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=200)),
                ('id_Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Estudiante')),
                ('id_Pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_OVA.Pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_Subtema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_OVA.Subtema'),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cod_grupo', models.CharField(max_length=10, unique=True)),
                ('fecha_creacion', models.DateField()),
                ('num_estudiantes', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('estudiantes', models.ManyToManyField(to='usuarios.Estudiante')),
                ('id_Docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Docente')),
                ('objetos_virtuales', models.ManyToManyField(to='Gestion_OVA.Objeto')),
            ],
        ),
    ]