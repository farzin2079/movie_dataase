# Generated by Django 4.1.2 on 2023-03-30 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_favorites_alter_profile_friends_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to='profiles/<django.db.models.query_utils.DeferredAttribute object at 0x00000271EEEAB3A0>'),
        ),
    ]
