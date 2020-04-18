from django.db import models

# Create your models here.

class InstituteModel(models.Model):
    name=models.CharField(max_length=256,blank=True)
    abriviation=models.CharField(max_length=256,blank=True)
    doe=models.DateField(null=True)
    area=models.CharField(max_length=256,blank=True)
    address=models.CharField(max_length=256,blank=True)
    buses=models.BooleanField(default=False)
    canteen=models.BooleanField(default=False)
    hostel=models.BooleanField(default=False)
    describe=models.TextField(blank=True)
    is_university=models.BooleanField(blank=True)
    affiliated_by=models.CharField(max_length=256,blank=True)
    website=models.CharField(max_length=256,blank=True)
    type=models.CharField(max_length=256,blank=True)
    logo=models.ImageField(upload_to="img/logo/",null=True,blank=True)
    country=models.CharField(max_length=256,blank=True)
    state=models.CharField(max_length=256,blank=True)
    city=models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.name

class InstitutePrincipal(models.Model):
    institute_id=models.OneToOneField(InstituteModel,on_delete=models.CASCADE,related_name="PRINCIPAL")
    name=models.CharField(max_length=256)
    experience=models.IntegerField(null=True)
    qualification=models.CharField(max_length=256,blank=True)
    details=models.TextField(blank=True)
    image=models.ImageField(upload_to="img/principal/",null=True,blank=True)

    def __str__(self):
        return self.name

class InstituteDirector(models.Model):
    institute_id=models.OneToOneField(InstituteModel,on_delete=models.CASCADE,related_name="DIRECTOR")
    name=models.CharField(max_length=256)
    experience=models.IntegerField(null=True)
    qualification=models.CharField(max_length=256,blank=True)
    details=models.TextField(blank=True)
    image=models.ImageField(upload_to="img/director/",null=True,blank=True)

    def __str__(self):
        return self.name

class InstituteTPO(models.Model):
    institute_id=models.OneToOneField(InstituteModel,on_delete=models.CASCADE,related_name="TPO")
    name=models.CharField(max_length=256)
    experience=models.IntegerField(null=True)
    qualification=models.CharField(max_length=256,blank=True)
    details=models.TextField(blank=True)
    image=models.ImageField(upload_to="img/tpo/",null=True,blank=True)

    def __str__(self):
        return self.name

class InstituteImages(models.Model):
    image=models.ImageField(upload_to="img/college/",null=True,blank=True)
    institute_id=models.ForeignKey(InstituteModel,on_delete=models.CASCADE,related_name="INSTITUTE_IMAGES")

# class Address(models.Model):
#     institute_id=models.OneToOneField(InstituteModel,on_delete=models.CASCADE,related_name="ADDRESS")
#     country=models.CharField(max_length=256,blank=True)
#     state=models.CharField(max_length=256,blank=True)
#     city=models.CharField(max_length=256,blank=True)
#     street=models.CharField(max_length=256,blank=True)
#     pincode=models.IntegerField(null=True,blank=True)
#     latitude=models.DecimalField(max_digits=8,decimal_places=8,null=True,blank=True)
#     longititude=models.DecimalField(max_digits=8,decimal_places=8,null=True,blank=True)
