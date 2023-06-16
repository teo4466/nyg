# Generated by Django 4.2.1 on 2023-06-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0026_combustible_importe'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitas',
            name='ciudad',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='visitas',
            name='imagen',
            field=models.ImageField(null=True, upload_to='visitas/'),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='estado',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
