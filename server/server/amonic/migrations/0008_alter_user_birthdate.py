# Generated by Django 4.2.6 on 2023-11-08 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("amonic", "0007_alter_user_birthdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(
                default=datetime.date(2023, 11, 8), verbose_name="Дата рождения"
            ),
        ),
    ]
