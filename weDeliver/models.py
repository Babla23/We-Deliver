from django.db import models

class Products(models.Model):
    prodId = models.AutoField(primary_key = True)
    brand = models.CharField(max_length=50)
    modelNo = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    price = models.FloatField()
    quatity = models.IntegerField()
    photo = models.ImageField(blank=True,upload_to='products/')
    pdate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=30)