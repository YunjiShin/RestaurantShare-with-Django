# Generated by Django 5.0.3 on 2024-05-09 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shareRes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("restaurant_name", models.CharField(max_length=100)),
                ("restaurant_link", models.CharField(max_length=500)),
                ("restaurant_content", models.TextField()),
                ("restaurant_keyword", models.CharField(max_length=50)),
                (
                    "category",
                    models.ForeignKey(
                        default=5,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="shareRes.category",
                    ),
                ),
            ],
        ),
    ]
