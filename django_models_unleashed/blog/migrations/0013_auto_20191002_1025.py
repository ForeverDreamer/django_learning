# Generated by Django 2.2.1 on 2019-10-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20191001_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'unique': 'This title is not unique, please try again.'}, help_text='Must be a unique title.', max_length=240, unique=True, verbose_name='Post title'),
        ),
    ]
