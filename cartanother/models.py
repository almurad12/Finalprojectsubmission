from django.db import models
from account.models import User
from service.models import Sheba
# Create your models here.

class Cartanother(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Sheba,on_delete=models.CASCADE)
    servicetitle =  models.CharField(max_length=300)
    serviceprice =  models.CharField(max_length=300)
    serviceuseridnum =  models.IntegerField(max_length=300)

class Cartanothernew(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Sheba,on_delete=models.CASCADE)
    servicetitle =  models.CharField(max_length=300)
    serviceprice =  models.CharField(max_length=300)
    serviceuseridnum =  models.IntegerField(max_length=300)

class Order(models.Model):
     cartid = models.IntegerField(max_length=300)
     serviceuserid = models.IntegerField(max_length=300)
     userid=models.IntegerField(max_length=300)
     serviceid=models.IntegerField(max_length=300)
     orderservicetitle=models.CharField(max_length=300)
     orderserviceprice=models.CharField(max_length=300)
     orderdate = models.DateField()
     orderaddress = models.CharField(max_length=300)
     orderphoneno = models.CharField(max_length=300)



class Ordernew(models.Model):
     cartid = models.IntegerField(max_length=300)
     serviceuserid = models.IntegerField(max_length=300)
     userid=models.IntegerField(max_length=300)
     serviceid=models.IntegerField(max_length=300)
     orderservicetitle=models.CharField(max_length=300)
     orderserviceprice=models.CharField(max_length=300)
     orderdate = models.DateField()
     time = models.TimeField(default=None)
     orderaddress = models.CharField(max_length=300)
     orderphoneno = models.CharField(max_length=300)
     accept_or_rejected = models.BooleanField(default=False)
     order_complete = models.BooleanField(default=False)
     order_final_complete= models.BooleanField(default=False)
     buyer_review_complete= models.BooleanField(default=False)
     seller_review_complete= models.BooleanField(default=False)