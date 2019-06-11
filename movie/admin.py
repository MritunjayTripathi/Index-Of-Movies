from django.contrib import admin

from movie.models import Movie, FeaturedMovie

admin.site.register(Movie)
admin.site.register(FeaturedMovie)
