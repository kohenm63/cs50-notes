# Generated by Django 4.2.5 on 2023-09-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cs50notes", "0002_lecturenote_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturenote",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="lecture_images/"),
        ),
    ]
