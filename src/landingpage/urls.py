from django.urls import path
from landingpage.views import LandingPage,Login,SignUp,Logout,AuthenticationUser

urlpatterns=[
    path('',LandingPage.as_view(),name="landingpage"),
    path('login/',Login.as_view(),name="login"),
    path('signup/',SignUp.as_view(),name="signup"),
    path('logout/',Logout.as_view(),name="logout"),
    path('authentication/',AuthenticationUser.as_view(),name="auth"),
]
