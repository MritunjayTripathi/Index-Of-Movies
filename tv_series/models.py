from django.db import models


class FeaturedTvShow(models.Model):
    tvseries_name = models.CharField(max_length=100)
    tvseries_icon = models.CharField(max_length=500, default="#")
    tvseries_link = models.CharField(max_length=1000, default="#")

    def __str__(self):
        return self.tvseries_name


class TvShow(models.Model):
    tvseries_name = models.CharField(max_length=100)
    tvseries_icon = models.CharField(max_length=500, default="#")
    lang = models.CharField(max_length=100, default="English")
    release_year = models.CharField(max_length=100, default="-")
    i_m_d_b = models.CharField(max_length=10, default="-")

    def __str__(self):
        return self.tvseries_name


class Season(models.Model):
    tv_series = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    season_no = models.CharField(max_length=100)
    release_year = models.CharField(max_length=100, default="-")
    i_m_d_b = models.CharField(max_length=10, default="-")

    def __str__(self):
        return self.tv_series.tvseries_name + self.season_no


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_name = models.CharField(max_length=100)

    episode_download_link_1080 = models.CharField(max_length=1000, default="#")
    episode_download_link_720 = models.CharField(max_length=1000, default="#")
    episode_download_link_480 = models.CharField(max_length=1000, default="#")
    episode_download_link_other = models.CharField(max_length=1000, default="#")

    episode_icon = models.CharField(max_length=500, default="#")
    i_m_d_b = models.CharField(max_length=10, default="-")

    def __str__(self):
        return self.episode_name
