# Generated by Django 4.2.6 on 2023-11-09 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("amonic", "0004_usercrashreport_userlog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(
                default=datetime.date(2023, 11, 9), verbose_name="Дата рождения"
            ),
        ),
    ]
