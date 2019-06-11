from django.shortcuts import render, get_object_or_404, render_to_response
import math
from movie.models import Movie, FeaturedMovie


# Create your views here.
def index(request, page_no):
    no_of_elements = 16
    page_no = int(page_no)
    starting_index = (page_no - 1) * no_of_elements
    last_index = page_no * no_of_elements

    total = Movie.objects.all().count()

    queryset1 = Movie.objects.all()[starting_index:last_index]

    last_page_no = math.ceil(total / no_of_elements)

    hide1 = True
    hide2 = True

    if page_no == 1:
        hide1 = False

    if page_no == last_page_no:
        hide2 = False

    next_page_no = page_no + 1
    previous_page_no = page_no - 1

    queryset2 = FeaturedMovie.objects.all()
    context = {
        'movies': queryset1,
        'featured_movie': queryset2,
        'page_no': page_no,
        'next_page_no': next_page_no,
        'previous_page_no': previous_page_no,
        'hide1': hide1,
        'hide2': hide2,
        'total': total,
        'last_page_no': last_page_no,

    }
    return render(request, 'movie/index.html', context)


def detail(request, movie_name):
    movie = get_object_or_404(Movie, movie_name=str(movie_name))
    return render(request, 'movie/detail.html', {'movie': movie})
