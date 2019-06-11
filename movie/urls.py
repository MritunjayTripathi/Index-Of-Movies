from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    url(r'^page(?P<page_no>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<movie_name>[\w\-\,\ ]+)/$', views.detail, name='detail'),
]
