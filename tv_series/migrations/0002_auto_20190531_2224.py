# Generated by Django 2.2.1 on 2019-05-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_download_link',
            field=models.CharField(default='#', max_length=500),
        ),
        migrations.AlterField(
            model_name='episode',
            name='episode_icon',
            field=models.CharField(default='#', max_length=500),
        ),
        migrations.AlterField(
            model_name='episode',
            name='i_m_d_b',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='season',
            name='i_m_d_b',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='season',
            name='release_year',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='i_m_d_b',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='lang',
            field=models.CharField(default='English', max_length=100),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='release_year',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='tvseries_icon',
            field=models.CharField(default='#', max_length=500),
        ),
    ]