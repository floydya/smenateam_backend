# Generated by Django 3.0.5 on 2020-04-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='api_key',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
