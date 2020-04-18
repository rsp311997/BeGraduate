from django.contrib import admin
from account.models import ProfileModel

# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['id','user','nickname','dob','country','state','city','occupation','schoolname','collegename','describe','is_active','profile_pic']

admin.site.register(ProfileModel,ProfileModelAdmin)
