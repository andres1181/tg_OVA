# Generated by Django 2.2.2 on 2019-11-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('username', models.CharField(max_length=10, verbose_name='NickName')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10, verbose_name='Contraseña')),
                ('codigo_docente', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('username', models.CharField(max_length=10, verbose_name='NickName')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10, verbose_name='Contraseña')),
                ('codigo_estudiante', models.CharField(max_length=10, unique=True)),
                ('plan', models.CharField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]