# Generated by Django 5.0 on 2023-12-12 14:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigateway', '0004_alter_logininfo_fid_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educator',
            name='EID',
            field=models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False),
        ),
    ]
