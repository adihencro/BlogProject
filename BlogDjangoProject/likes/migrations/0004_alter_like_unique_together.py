# Generated by Django 5.0.3 on 2024-03-19 13:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("likes", "0003_like_comment_id_like_post_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("liked_by", "comment_id"), ("liked_by", "post_id")},
        ),
    ]
