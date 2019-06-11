from django.contrib import admin

from .models import TvShow, Season, Episode, FeaturedTvShow

admin.site.register(TvShow)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(FeaturedTvShow)
