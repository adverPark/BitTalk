# Generated by Django 4.2 on 2023-05-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "남"), ("female", "여")],
                max_length=10,
                null=True,
            ),
        ),
    ]
