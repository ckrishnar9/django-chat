# Generated by Django 5.0.4 on 2024-05-03 11:25

import server.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.FileField(
                blank=True, null=True, upload_to=server.models.category_icon_upload_path
            ),
        ),
        migrations.AlterField(
            model_name="server",
            name="description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="server",
            name="member",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]