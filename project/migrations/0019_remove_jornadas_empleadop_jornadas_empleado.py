# Generated by Django 4.2.1 on 2023-06-11 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_remove_capacitacione_empleado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jornadas',
            name='empleadop',
        ),
        migrations.AddField(
            model_name='jornadas',
            name='empleado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.empleados'),
        ),
    ]