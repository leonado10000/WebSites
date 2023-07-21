# Generated by Django 4.1.7 on 2023-06-13 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0002_post_tags_alter_post_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="tags",
            name="name",
            field=models.CharField(default="Tag", max_length=30),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 13, 23, 6, 6, 956597)
            ),
        ),
    ]