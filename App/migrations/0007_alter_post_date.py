# Generated by Django 4.1.7 on 2023-06-13 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0006_remove_post_tags_post_p_tags_post_id_alter_post_p_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 13, 23, 17, 51, 971546)
            ),
        ),
    ]
