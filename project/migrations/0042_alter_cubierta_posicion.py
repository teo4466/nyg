# Generated by Django 4.2.1 on 2023-06-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0041_alter_cubierta_posicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cubierta',
            name='posicion',
            field=models.CharField(max_length=50),
        ),
    ]