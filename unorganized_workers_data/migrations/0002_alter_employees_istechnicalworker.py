# Generated by Django 4.1 on 2022-08-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unorganized_workers_data", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employees",
            name="isTechnicalWorker",
            field=models.BooleanField(default=False),
        ),
    ]
