from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'tv_series'

urlpatterns = [
    url(r'^page(?P<page_no>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<tvshows>[a-zA-Z0-9- ]+)/$', views.detailShow, name='detail'),
    url(r'^(?P<tvshows>[a-zA-Z0-9- ]+)/season(?P<season_no>[a-zA-Z0-9- ]+)/$', views.detailSeason, name='detailSeason'),
    url(r'^(?P<tvshow>[a-zA-Z0-9- ]+)/season(?P<season_name>[a-zA-Z0-9- ]+)/(?P<episode_name>[a-zA-Z0-9- ,]+)/$', views.detailEpisode,name='detailEpisode'),
]
