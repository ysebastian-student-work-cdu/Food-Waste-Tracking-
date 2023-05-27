# Generated by Django 4.1.7 on 2023-05-27 02:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audit", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodForm",
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
                ("nameofItem1", models.CharField(max_length=100)),
                ("quantity1", models.IntegerField()),
                ("nameofItem2", models.CharField(max_length=100)),
                ("quantity2", models.IntegerField()),
                ("nameofItem3", models.CharField(max_length=100)),
                ("quantity3", models.IntegerField()),
            ],
        ),
    ]
