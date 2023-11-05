# Generated by Django 4.2.6 on 2023-11-02 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("amonic", "0005_alter_user_birthdate"),
        ("flight", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CabinTypes",
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
                ("name", models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name="Tickets",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("passport_number", models.CharField(max_length=255)),
                ("confirmed", models.SmallIntegerField(default=False)),
                ("booking_reference", models.SmallIntegerField(default=False)),
                (
                    "cabin_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tickets.cabintypes",
                    ),
                ),
                (
                    "passport_county",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="amonic.country"
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flight.schedule",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
