from django.db import models
from django.contrib.auth.models import User
from institute.models import InstituteModel
# Create your models here.
class Review(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="GIVEN_REVIEW")
    institite_id=models.ForeignKey(InstituteModel,on_delete=models.CASCADE,related_name="REVIEWS")
    rate_principal=models.IntegerField(null=True,blank=True)
    rate_director=models.IntegerField(null=True,blank=True)
    rate_tpo=models.IntegerField(null=True,blank=True)
    rate_college=models.IntegerField(null=True,blank=True)
    your_view=models.TextField(blank=True)
    pros=models.TextField(blank=True)
    cons=models.TextField(blank=True)
    datetime=models.DateTimeField(null=True)
