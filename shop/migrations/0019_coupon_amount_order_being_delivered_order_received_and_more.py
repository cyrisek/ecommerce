# Generated by Django 4.1.6 on 2023-02-09 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0018_order_coupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="coupon",
            name="amount",
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="being_delivered",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="received",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="ref_code",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="refund_granted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="refund_requested",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "stripe_customer_id",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("one_click_purchasing", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Refund",
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
                ("reason", models.TextField()),
                ("accepted", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("street_address", models.CharField(max_length=100)),
                ("apartment_address", models.CharField(max_length=100)),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("postcode", models.CharField(max_length=100)),
                (
                    "address_type",
                    models.CharField(
                        choices=[("B", "Billing"), ("S", "Shipping")], max_length=1
                    ),
                ),
                ("default", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shipping_address",
                to="shop.address",
            ),
        ),
    ]
