# Generated by Django 3.0.5 on 2020-04-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.CharField(max_length=10000, verbose_name='image'),
        ),
    ]
