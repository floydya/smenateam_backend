# Generated by Django 3.0.5 on 2020-04-12 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200412_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='type',
        ),
    ]
