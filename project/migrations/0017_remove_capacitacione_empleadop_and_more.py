# Generated by Django 4.2.1 on 2023-06-11 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_remove_jornadas_empleadop_jornadas_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitacione',
            name='empleadop',
        ),
        migrations.AddField(
            model_name='capacitacione',
            name='empleado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.empleados'),
            preserve_default=False,
        ),
    ]