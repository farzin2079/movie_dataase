# Generated by Django 4.1.2 on 2023-03-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='user',
            field=models.ManyToManyField(related_name='favorite_user', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='hello, world!', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites_set', to='users.favorites'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to='profiles/<django.db.models.query_utils.DeferredAttribute object at 0x0000017FBD43B3A0>'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wishlists',
            field=models.ManyToManyField(related_name='wishlist_set', to='users.whishlist'),
        ),
        migrations.AlterField(
            model_name='whishlist',
            name='user',
            field=models.ManyToManyField(related_name='wishlist_user', to='users.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='friends_set', to='users.profile'),
        ),
    ]
