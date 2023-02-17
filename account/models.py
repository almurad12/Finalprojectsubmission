from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_buyer= models.BooleanField('Is buyer', default=False)
    is_seller =models.BooleanField('Is seller', default=False)


class Review(models.Model):
    reviewgivenid= models.IntegerField(max_length=20)
    reviewreceiveid = models.IntegerField(max_length=20)
    comment = models.TextField(max_length=300)
    rating = models.IntegerField(max_length=20)
    bol = models.BooleanField(default=0)


# class Reviewpost(models.Model):
#     reviewgivenid= models.ForeignKey(User,on_delete=models.CASCADE)
#     reviewreceiveid =models.ForeignKey(User,on_delete=models.CASCADE)
#     comment = models.TextField(max_length=300)
#     rating = models.IntegerField()
#     bol = models.BooleanField(default=0)