# Generated by Django 5.0.2 on 2024-02-17 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_author_alter_post_photo_post_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_name", models.CharField(max_length=63)),
                ("text", models.TextField()),
                ("created_time", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
        ),
    ]