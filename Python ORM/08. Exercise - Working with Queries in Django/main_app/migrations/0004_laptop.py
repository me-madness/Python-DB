# Generated by Django 5.0.6 on 2024-07-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_artworkgallery_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('ASUS', 'ASUS'), ('ACER', 'ACER'), ('APPLE', 'APPLE'), ('LENOVO', 'LENOVO'), ('DELL', 'DELL')], max_length=20)),
                ('processor', models.CharField(max_length=100)),
                ('memory', models.PositiveIntegerField(help_text='Memory in GB')),
                ('storage', models.PositiveIntegerField(help_text='Storage in GB')),
                ('operation_system', models.CharField(choices=[('WINDOWS', 'WINDOWS'), ('MACOS', 'MACOS'), ('LINUX', 'LINUX'), ('CHROME_OS', 'CHROME_OS')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
