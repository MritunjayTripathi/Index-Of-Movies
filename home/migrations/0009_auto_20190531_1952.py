# Generated by Django 2.2.1 on 2019-05-31 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190531_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='season',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.RemoveField(
            model_name='season',
            name='tv_series',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='TvSeries',
        ),
    ]