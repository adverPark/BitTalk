# Generated by Django 4.2 on 2023-05-03 07:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coin_kind", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="coinkind",
            options={"verbose_name_plural": "코인 종류"},
        ),
    ]
