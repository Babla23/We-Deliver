# Generated by Django 3.0.5 on 2020-05-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weDeliver', '0003_auto_20200509_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
    ]