# Generated by Django 4.1 on 2022-08-17 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "unorganized_workers_data",
            "0003_alter_employees_address_alter_employees_email_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="employees",
            name="cvUrl",
            field=models.CharField(blank=True, max_length=2080),
        ),
    ]
