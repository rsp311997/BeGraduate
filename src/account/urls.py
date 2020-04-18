from  django.urls import path
from account.views import Profile,EditProfile

urlpatterns=[
    path('profile/',Profile.as_view(),name="profile"),
    path('profile/edit/<int:id>',EditProfile.as_view(),name="editprofile")
]
