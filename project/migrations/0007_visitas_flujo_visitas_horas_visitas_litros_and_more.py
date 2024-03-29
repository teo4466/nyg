# Generated by Django 4.2.1 on 2023-08-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_checkcamion_imagen_alter_checkcamion_imagen2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitas',
            name='flujo',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='visitas',
            name='horas',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='visitas',
            name='litros',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='imagen',
            field=models.ImageField(default='', upload_to='visitas/'),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='observacion',
            field=models.TextField(default='', max_length=300),
        ),
    ]
