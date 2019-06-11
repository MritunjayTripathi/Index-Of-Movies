# Generated by Django 2.2.1 on 2019-05-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_series', '0002_auto_20190531_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='episode_download_link',
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_download_link_1080',
            field=models.CharField(default='#', max_length=1000),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_download_link_480',
            field=models.CharField(default='#', max_length=1000),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_download_link_720',
            field=models.CharField(default='#', max_length=1000),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_download_link_other',
            field=models.CharField(default='#', max_length=1000),
        ),
    ]
