# Generated by Django 4.1.7 on 2023-05-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Scotopia", "0010_remove_scotops_scoto_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="scotops",
            name="scoto_category",
            field=models.ForeignKey(
                default=404,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="Scotopia.category",
            ),
        ),
    ]