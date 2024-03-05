from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class CustomUser(AbstractBaseUser):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email
    
class Packages(models.Model):
    place_image = models.ImageField(upload_to='package_images/')
    place_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.place_name
    
class SubPackage(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    sub_place_image = models.ImageField(upload_to='subpackage_images/')
    sub_place_name = models.CharField(max_length=255)
    sub_description = models.TextField()

    def __str__(self):
        return self.sub_place_name

class Destination(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='destination_images/')
    discount_percentage = models.PositiveIntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name    