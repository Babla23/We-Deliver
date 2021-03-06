# Generated by Django 3.0.5 on 2020-05-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prodId', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('modelNo', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('quatity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='products/')),
                ('pdate', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
