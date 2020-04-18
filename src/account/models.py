from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfileModel(models.Model):
    nickname=models.CharField(max_length=100,blank=True)
    dob=models.DateField(null=True,blank=True)
    country=models.CharField(max_length=256,blank=True)
    state=models.CharField(max_length=256,blank=True)
    city=models.CharField(max_length=256,blank=True)
    schoolname=models.CharField(max_length=256,blank=True)
    collegename=models.CharField(max_length=256,blank=True)
    occupation=models.CharField(max_length=256,blank=True)
    contact=models.IntegerField(blank=True,null=True)
    describe=models.TextField(blank=True)
    is_active=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="PROFILE")
    profile_pic=models.ImageField(null=True,blank=True)
