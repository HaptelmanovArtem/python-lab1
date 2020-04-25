# Generated by Django 3.0.5 on 2020-04-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=100, verbose_name='image name')),
                ('image_url', models.ImageField(upload_to='', verbose_name='image')),
                ('image_like', models.IntegerField(verbose_name='count like')),
            ],
        ),
    ]
