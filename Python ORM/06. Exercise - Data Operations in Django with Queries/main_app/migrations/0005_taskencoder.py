# Generated by Django 5.0.6 on 2024-06-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskEncoder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
