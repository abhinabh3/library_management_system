# Generated by Django 5.1.1 on 2024-09-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
