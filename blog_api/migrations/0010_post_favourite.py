# Generated by Django 3.2.3 on 2021-06-08 05:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_api', '0009_auto_20210601_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='fav_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
