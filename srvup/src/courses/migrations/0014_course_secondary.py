# Generated by Django 2.2 on 2019-08-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('courses', '0013_auto_20190827_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='secondary',
            field=models.ManyToManyField(blank=True, related_name='secondary_category', to='categories.Category'),
        ),
    ]
