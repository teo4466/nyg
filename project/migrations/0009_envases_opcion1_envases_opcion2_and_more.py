# Generated by Django 4.2.1 on 2023-08-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_envases'),
    ]

    operations = [
        migrations.AddField(
            model_name='envases',
            name='opcion1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='envases',
            name='opcion2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='envases',
            name='diereccion',
            field=models.CharField(max_length=100),
        ),
    ]
