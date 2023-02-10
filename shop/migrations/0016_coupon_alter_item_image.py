# Generated by Django 4.1.6 on 2023-02-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_alter_item_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
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
                ("code", models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
