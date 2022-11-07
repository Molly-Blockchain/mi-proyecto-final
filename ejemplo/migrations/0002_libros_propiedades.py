# Generated by Django 4.1.2 on 2022-11-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=30)),
                ('valor', models.CharField(max_length=20)),
            ],
        ),
    ]