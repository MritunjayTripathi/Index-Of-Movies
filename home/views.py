from django.db.models import Q
from django.shortcuts import render

from movie.models import FeaturedMovie, Movie
from tv_series.models import FeaturedTvShow, TvShow
from .models import Featured


def index(request):
    x = FeaturedMovie.objects.all()
    queryset1 = FeaturedMovie.objects.all()
    queryset2 = FeaturedTvShow.objects.all()
    context = {
        'movies': queryset1,
        'tv_series': queryset2,
        'featured_videos': Featured.objects.all(),
    }
    return render(request, 'home/index.html', context)


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match_movies = Movie.objects.filter(Q(movie_name__icontains=srch))
            match_tv_series = TvShow.objects.filter(Q(tvseries_name__icontains=srch))

            return render(request, 'home/search_result.html',
                          {'match_movies': match_movies, 'match_tv_series': match_tv_series})

    return render(request, 'home/index.html')
