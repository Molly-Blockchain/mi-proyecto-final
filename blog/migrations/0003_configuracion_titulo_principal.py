# Generated by Django 4.1.2 on 2022-11-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_configuracion_construido_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='titulo_principal',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
