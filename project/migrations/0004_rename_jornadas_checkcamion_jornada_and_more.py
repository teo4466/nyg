# Generated by Django 4.2.1 on 2023-06-03 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_accesorioscamion_accesoriosempleado_camiones_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkcamion',
            old_name='Jornadas',
            new_name='Jornada',
        ),
        migrations.RenameField(
            model_name='checkcamion',
            old_name='Cubiertas',
            new_name='cubiertas',
        ),
        migrations.RenameField(
            model_name='checkcamion',
            old_name='extructura',
            new_name='estructura',
        ),
        migrations.RenameField(
            model_name='checkcamion',
            old_name='nivelFluidos',
            new_name='nivelfluidos',
        ),
    ]
