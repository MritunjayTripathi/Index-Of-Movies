from django.db import models


class Featured(models.Model):
    video_name = models.CharField(max_length=100)
    video_icon = models.CharField(max_length=1000, default="#")
    video_type = models.CharField(max_length=1000, default="movie")

    def __str__(self):
        return self.video_type + " : " + self.video_name
