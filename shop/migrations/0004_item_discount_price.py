# Generated by Django 4.1.6 on 2023-02-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_item_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="discount_price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
