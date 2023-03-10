# Generated by Django 4.1.6 on 2023-02-07 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "shop",
            "0012_rename_apartment_adress_billingadress_apartment_address_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BillingAdress",
            new_name="BillingAddress",
        ),
        migrations.AddField(
            model_name="order",
            name="billing_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.billingaddress",
            ),
        ),
    ]
