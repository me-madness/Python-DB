# Generated by Django 5.0.6 on 2024-06-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_eventregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='event_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='participant_name',
            field=models.CharField(max_length=60),
        ),
    ]
