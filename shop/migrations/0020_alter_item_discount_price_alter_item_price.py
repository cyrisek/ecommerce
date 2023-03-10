# Generated by Django 4.1.6 on 2023-02-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0019_coupon_amount_order_being_delivered_order_received_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="discount_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
