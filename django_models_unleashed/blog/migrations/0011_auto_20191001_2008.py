# Generated by Django 2.2.1 on 2019-10-01 12:08

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191001_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[blog.models.validate_author_email, blog.models.validate_justin]),
        ),
    ]
