from django.db import models


class FeaturedMovie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_icon = models.CharField(max_length=500, default="#")
    movie_link = models.CharField(max_length=1000, default="#")

    def __str__(self):
        return self.movie_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_download_link_1080 = models.CharField(max_length=1000, default="#")
    movie_download_link_720 = models.CharField(max_length=1000, default="#")
    movie_download_link_480 = models.CharField(max_length=1000, default="#")
    movie_download_link_other = models.CharField(max_length=1000, default="#")

    movie_icon = models.CharField(max_length=500, default="#")
    lang = models.CharField(max_length=100, default="English")
    description = models.CharField(max_length=5000, default="-")
    i_m_d_b = models.CharField(max_length=10, default="-")
    release_year = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.movie_name
