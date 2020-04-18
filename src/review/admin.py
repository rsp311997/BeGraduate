from django.contrib import admin
from review.models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=['id','user_id','institite_id','rate_college','rate_principal','rate_director','rate_tpo','your_view','pros','cons']


admin.site.register(Review,ReviewAdmin)
