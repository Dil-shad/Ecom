
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


# todo
class ContactModel(models.Model):
    pname = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=560)

    def __str__(self):
        return self.pname


class ProductCategory(models.Model):
    category = models.CharField(max_length=220)

    def __str__(self):
        return self.category


class ProductModel(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50)
    product_title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=150, null=True, blank=True)
    price = models.IntegerField(default=1011)
    quantity = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="image", null=True, blank=True)

    def __str__(self):
        return self.product_name


class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prdt = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, null=True)

    item = models.CharField(max_length=50, null=True)

    def __int__(self):
        return self.user
