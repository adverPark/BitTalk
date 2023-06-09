# Generated by Django 4.2 on 2023-05-03 13:16

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_category_options_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.fields.related.ManyToManyField,
                related_name="Posts",
                to="blog.category",
            ),
        ),
    ]
