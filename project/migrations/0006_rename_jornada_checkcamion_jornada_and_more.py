# Generated by Django 4.2.1 on 2023-06-04 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_capacitacion_empleadop_capacitacione'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkcamion',
            old_name='Jornada',
            new_name='jornada',
        ),
        migrations.RenameField(
            model_name='visitas',
            old_name='momentorecivida',
            new_name='momentorecibida',
        ),
    ]