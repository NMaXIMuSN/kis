# Generated by Django 4.2.6 on 2023-11-09 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
