from django.contrib import admin
from institute.models import InstituteModel,InstitutePrincipal,InstituteDirector,InstituteTPO,InstituteImages#,Address

# Register your models here.
class InstituteModelAdmin(admin.ModelAdmin):
    list_display=[
    'id',
    'name',
    'abriviation',
    'doe',
    'area',
    'address',
    'buses',
    'canteen',
    'describe',
    'is_university',
    'affiliated_by',
    'website',
    'type',
    'logo',
    'city',
    'country',
    'state',
    ]

class InstitutePrincipalAdmin(admin.ModelAdmin):
    list_display=[
    'id',
    'institute_id',
    'name',
    'experience',
    'qualification',
    'details',
    'image'
    ]

class InstituteDirectorAdmin(admin.ModelAdmin):
    list_display=[
    'id',
    'institute_id',
    'name',
    'experience',
    'qualification',
    'details',
    'image'
    ]

class InstituteTPOAdmin(admin.ModelAdmin):
    list_display=[
    'id',
    'institute_id',
    'name',
    'experience',
    'qualification',
    'details',
    'image'
    ]

class InstituteImagesAdmin(admin.ModelAdmin):
    list_display=[
    'id',
    'institute_id',
    'image',
    ]

# class AddressAdmin(admin.ModelAdmin):
#     list_display=[
#     'id',
#     'institute_id',
#     'country',
#     'state',
#     'city',
#     'street',
#     'pincode',
#     'latitude',
#     'longititude',
#     ]


admin.site.register(InstituteModel,InstituteModelAdmin)
admin.site.register(InstitutePrincipal,InstitutePrincipalAdmin)
admin.site.register(InstituteDirector,InstituteDirectorAdmin)
admin.site.register(InstituteTPO,InstituteTPOAdmin)
admin.site.register(InstituteImages,InstituteImagesAdmin)
# admin.site.register(Address,AddressAdmin)
