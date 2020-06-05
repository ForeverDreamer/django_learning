# Generated by Django 2.2.1 on 2019-10-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=240, verbose_name='Post title'),
        ),
    ]