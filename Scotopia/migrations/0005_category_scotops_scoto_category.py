# Generated by Django 4.1.7 on 2023-05-16 12:00

import Scotopia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Scotopia", "0004_user_remove_scotops_scoto_tag1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("cat_id", models.IntegerField()),
                ("cat_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="scotops",
            name="scoto_category",
            field=models.CharField(
                default="Uncategorised",
                max_length=1000,
                verbose_name=Scotopia.models.Category,
            ),
        ),
    ]
