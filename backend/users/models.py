from django.db import models
from django.contrib.auth.models import User
from playlists.models import Movie_playlist, Tv_playlist
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='profile_User')
    username = models.CharField(max_length=20)
    friends = models.ManyToManyField("Profile", related_name='friends_set')
    wishlists = models.ManyToManyField("Whishlist", related_name='wishlist_set')
    favorites = models.ManyToManyField("Favorites", related_name='favorites_set')
    profile_image = models.ImageField(upload_to=f'profiles/{User.username}', default='/user.png', null=True, blank=True)
    movies_playlists = models.ManyToManyField(Movie_playlist, related_name='movies_playlists')
    tvs_playlists = models.ManyToManyField(Tv_playlist, related_name='tvs_playlists')
    bio = models.CharField(max_length=200, blank=True, null=True, default='hello, world!')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Whishlist(models.Model):
    show = models.CharField(max_length=1000)
    user = models.ManyToManyField(Profile, related_name='wishlist_user')

class favorites(models.Model):
    show = models.CharField(max_length=1000)
    user = models.ManyToManyField(Profile, related_name="favorite_user")