# Generated by Django 2.2.1 on 2019-05-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_download_link', models.CharField(max_length=500)),
                ('movie_icon', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TvSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvseries_name', models.CharField(max_length=100)),
                ('tvseries_icon', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_no', models.CharField(max_length=100)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.TvSeries')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_name', models.CharField(max_length=100)),
                ('episode_download_link', models.CharField(max_length=500)),
                ('episode_icon', models.CharField(max_length=500)),
                ('episode_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Season')),
            ],
        ),
    ]
