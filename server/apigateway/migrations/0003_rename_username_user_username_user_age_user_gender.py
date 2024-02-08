# Generated by Django 5.0 on 2023-12-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apigateway", "0002_remove_assignment_timestamp_assignment_deadline_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="username",
            new_name="UserName",
        ),
        migrations.AddField(
            model_name="user",
            name="Age",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="Gender",
            field=models.CharField(default="male", max_length=10),
        ),
    ]