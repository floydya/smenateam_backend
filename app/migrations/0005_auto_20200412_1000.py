# Generated by Django 3.0.5 on 2020-04-12 07:00

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_check_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to=app.models.upload_to),
        ),
    ]
