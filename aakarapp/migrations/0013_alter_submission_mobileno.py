# Generated by Django 4.1 on 2022-12-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aakarapp", "0012_remove_submission_mail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission", name="mobileNo", field=models.IntegerField(),
        ),
    ]