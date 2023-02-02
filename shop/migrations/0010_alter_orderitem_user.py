# Generated by Django 4.1.6 on 2023-02-02 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0009_orderitem_ordered_orderitem_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
