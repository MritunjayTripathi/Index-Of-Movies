# Generated by Django 2.2.1 on 2019-06-02 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_series', '0004_featuredtvshow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featuredtvshow',
            old_name='tvseries_movie_icon',
            new_name='tvseries_icon',
        ),
    ]
