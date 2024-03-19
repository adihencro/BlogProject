# Generated by Django 5.0.3 on 2024-03-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("likes", "0002_initial"),
        ("posts", "0003_alter_post_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(related_name="posts", to="likes.like"),
        ),
    ]
