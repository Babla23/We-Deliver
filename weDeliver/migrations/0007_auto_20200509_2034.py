# Generated by Django 3.0.5 on 2020-05-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weDeliver', '0006_auto_20200509_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
