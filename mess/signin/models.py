from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    password = models.TextField()
    gender = models.TextField(max_length=12)
    
class UploadImage(models.Model):
    image=models.ImageField(upload_to='picture')    