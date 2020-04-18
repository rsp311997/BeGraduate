from django.urls import path,include
from institute.views import Home, Detail,Pics,Description

urlpatterns=[
    path('',Home.as_view(),name="home"),
    path('detail/<int:id>/',Detail.as_view(),name="detail"),
    path('institute/pics/<int:id>/',Pics.as_view(),name="institute-pics"),
    path('institute/description/<int:id>/',Description,name="institute-description"),

    path('reviews/<int:id>/',include('review.urls')),
]
