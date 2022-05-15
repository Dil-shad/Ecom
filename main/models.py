
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserEx(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=30)
    place = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image/user', null=True, blank=True)
