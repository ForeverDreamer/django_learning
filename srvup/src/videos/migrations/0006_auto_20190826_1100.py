# Generated by Django 2.2 on 2019-08-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20190823_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]