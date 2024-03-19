# Generated by Django 5.0.3 on 2024-03-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_initial"),
        ("likes", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="likes",
            field=models.ManyToManyField(related_name="comments", to="likes.like"),
        ),
    ]
