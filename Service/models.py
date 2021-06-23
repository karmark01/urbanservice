from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djrichtextfield.models import RichTextField


# Create your models here.

class Uuser(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    profile = models.ImageField(null=True, blank=True, upload_to="static/images")
    role = models.CharField(max_length=10)
    joining_date = models.DateField(null=True, blank=True)


class service(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Uuser, on_delete=models.CASCADE, related_name='user_id')
    type = models.CharField(max_length=20, null=True)
    date = models.DateField(auto_now_add=True, blank=True)
    Time = models.TimeField(auto_now_add=True, blank=True)
    fees = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    heading = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500)


class category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)


# class Requests(models.Model):
#     req = models.AutoField('ID',primary_key=True)
#     uid = models.ForeignKey(Uuser, on_delete=models.CASCADE, related_name='uid_id')
#     sid = models.ForeignKey(service, on_delete=models.CASCADE, related_name='sid_id')

class Requestss(models.Model):
    req = models.AutoField('ID',primary_key=True)
    uid = models.ForeignKey(Uuser, on_delete=models.CASCADE, related_name='uid_id')
    sid = models.ForeignKey(service, on_delete=models.CASCADE, related_name='sid_id')

class requests(models.Model):
    req = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Uuser, on_delete=models.CASCADE, related_name='u_id')
    sid = models.ForeignKey(service, on_delete=models.CASCADE, related_name='s_id')