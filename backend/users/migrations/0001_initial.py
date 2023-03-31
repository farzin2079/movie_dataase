# Generated by Django 4.1.2 on 2023-03-27 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.CharField(max_length=5000)),
                ('user', models.ManyToManyField(related_name='favorite_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Whishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.CharField(max_length=5000)),
                ('user', models.ManyToManyField(related_name='wishlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, default='static/img/profile_default.png', null=True, upload_to='profiles/<django.db.models.query_utils.DeferredAttribute object at 0x00000186C3A97310>')),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('favorites', models.ManyToManyField(related_name='favorites', to='users.favorites')),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movies_playlists', models.ManyToManyField(related_name='movies_playlists', to='playlists.movie_playlist')),
                ('tvs_playlists', models.ManyToManyField(related_name='tvs_playlists', to='playlists.tv_playlist')),
                ('wishlists', models.ManyToManyField(related_name='wishlist', to='users.whishlist')),
            ],
        ),
    ]
