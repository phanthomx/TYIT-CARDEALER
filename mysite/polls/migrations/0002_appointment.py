# Generated by Django 4.2.3 on 2024-02-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("name", models.CharField(max_length=15)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=12)),
                ("model_name", models.CharField(max_length=15)),
                ("registration_number", models.CharField(max_length=20)),
                ("appointment_date", models.DateField()),
                ("appointment_time", models.TimeField()),
                ("count", models.IntegerField()),
            ],
        ),
    ]
