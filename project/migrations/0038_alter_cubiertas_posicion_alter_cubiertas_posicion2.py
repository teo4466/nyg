# Generated by Django 4.2.1 on 2023-06-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0037_rename_fechacolocacion_cubiertas_fechac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cubiertas',
            name='posicion',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cubiertas',
            name='posicion2',
            field=models.CharField(default=True, max_length=20),
        ),
    ]