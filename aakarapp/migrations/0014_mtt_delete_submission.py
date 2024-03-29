# Generated by Django 4.1.3 on 2023-01-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aakarapp", "0013_alter_submission_mobileno"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mtt",
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
                ("email", models.CharField(max_length=200)),
                ("email1", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=50)),
                ("contact", models.IntegerField()),
                ("year", models.CharField(max_length=200)),
                ("ref", models.CharField(max_length=100)),
                ("colg", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(name="Submission",),
    ]
