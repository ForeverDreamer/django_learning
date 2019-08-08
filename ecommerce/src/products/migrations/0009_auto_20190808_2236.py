# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-08 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
