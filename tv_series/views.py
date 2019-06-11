from django.shortcuts import render, get_object_or_404
import math
from tv_series.models import TvShow, FeaturedTvShow, Season, Episode


def index(request, page_no):
    no_of_elements = 4
    page_no = int(page_no)
    starting_index = (page_no - 1) * no_of_elements
    last_index = page_no * no_of_elements

    total = TvShow.objects.all().count()

    queryset1 = TvShow.objects.all()[starting_index:last_index]

    last_page_no = math.ceil(total / no_of_elements)

    hide1 = True
    hide2 = True

    if page_no == 1:
        hide1 = False

    if page_no == last_page_no:
        hide2 = False

    next_page_no = page_no + 1
    previous_page_no = page_no - 1

    queryset2 = FeaturedTvShow.objects.all()

    context = {
        'tv_series': queryset1,
        'featured_tvshow': queryset2,
        'page_no': page_no,
        'next_page_no': next_page_no,
        'previous_page_no': previous_page_no,
        'hide1': hide1,
        'hide2': hide2,
        'total': total,
        'last_page_no': last_page_no,
    }
    return render(request, 'tv_series/index.html', context)


def detailShow(request, tvshows):
    series = TvShow.objects.get(tvseries_name__exact=tvshows)
    tv_series = get_object_or_404(TvShow, pk=series.id)
    return render(request, 'tv_series/detail.html', {'tv_series': tv_series, 'info': tvshows})


def detailSeason(request, tvshows, season_no):
    series = TvShow.objects.get(tvseries_name__exact=tvshows)
    tv_series_season = series.season_set.get(season_no__exact=str(season_no))

    return render(request, 'tv_series/season_detail.html',
                  {'tv_series_season': tv_series_season, 'series': series})


def detailEpisode(request, tvshow, season_name, episode_name):
    episode = get_object_or_404(Episode, episode_name__exact=episode_name)
    season = tvshow + season_name

    return render(request, 'tv_series/episode_detail.html',
                  {'season': season, 'episode': episode, 'tvshow': tvshow, })
