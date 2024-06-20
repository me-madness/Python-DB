# Generated by Django 5.0.6 on 2024-06-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_weatherforecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('cook_time', models.PositiveBigIntegerField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]