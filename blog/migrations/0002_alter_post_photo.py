# Generated by Django 5.0.2 on 2024-02-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="photo",
            field=models.FileField(upload_to="blog/media/user_post_uploads/"),
        ),
    ]
