# Generated by Django 4.2.1 on 2023-06-13 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_alter_checkcamion_camion_alter_combustible_camion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitas',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='visitas',
            name='jornada',
        ),
        migrations.AddField(
            model_name='visitas',
            name='empleado',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='project.empleados'),
        ),
        migrations.AlterField(
            model_name='jornadas',
            name='horasextras',
            field=models.CharField(default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='jornadas',
            name='kmllegada',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='jornadas',
            name='salida',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='jornadas',
            name='viaticos',
            field=models.CharField(default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='cliente',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='project.clientes'),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='momentocumplida',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='momentorecibida',
            field=models.CharField(default=True, max_length=50),
        ),
    ]