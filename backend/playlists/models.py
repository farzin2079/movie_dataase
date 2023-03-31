from django.db import models
from django.contrib.auth.models import User


class Movie_playlist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.CharField(max_length=5000)
    likes = models.ManyToManyField(User, related_name="movie_list_likes")

class Tv_playlist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.CharField(max_length=5000)
    likes = models.ManyToManyField(User, related_name="tv_list_likes")