# Generated by Django 4.1.6 on 2023-02-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_item_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="quantity",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
