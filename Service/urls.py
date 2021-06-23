
from django.contrib import admin
from django.urls import path,re_path
from . import views
from .views import home,Login,register,Aheadservice,service,postservice,uprofile,callme,showservices,logout,bookmyservice
urlpatterns = [
    path('', home.Home.as_view(),name='Home'),
    path('/<str:id1>/', home.Home.as_view(),name='Home'),

    path('Login', Login.Login.as_view(),name='Login'),
    path('Logout', logout.logout.as_view(), name='logout'),
    path('register/',register.register.as_view(),name='register'),
    path('register/<int:id>/', register.register.as_view(), name='register'),
    path('profile/',uprofile.userprofile.as_view(),name='profile'),
    path('service/', service.services.as_view(), name='service'),
    path('postservice/', postservice.postservice.as_view(), name='postservice'),
    path('callme/',callme.callme.as_view(),name='callme'),
    path('Aheadservice/',Aheadservice.Aheadservice.as_view(),name='Aheadservice'),
    path('Aheadservice/<int:id>/', Aheadservice.Aheadservice.as_view(), name='Aheadservice'),
    path('showervices',showservices.showservices.as_view(),name="showservices"),
    path('bookmyservice', bookmyservice.Bookmyservice.as_view(), name="bookmyservice"),
    path('bookmyservice/<int:id>/', bookmyservice.Bookmyservice.as_view(), name="bookmyservice"),
    path('bookmyservice/<int:req>/', bookmyservice.Bookmyservice.as_view(), name="bookmyservice")
]
