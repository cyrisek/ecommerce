# Generated by Django 4.1.6 on 2023-02-08 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0013_rename_billingadress_billingaddress_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="billingaddress",
            name="country",
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("stripe_charge_id", models.CharField(max_length=50)),
                ("amount", models.FloatField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.payment",
            ),
        ),
    ]
