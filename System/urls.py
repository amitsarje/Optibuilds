"""optibuilds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from .import views
from django.conf.urls import url

urlpatterns = [
#    url( r'$', views.Check_Fields,name ='check_fields'),
   url( r'^$', views.Login,name ='login') ,
   url( r'^home/$', views.Homepage,name ='homepage') ,
   url( r'^scrapper/$', views.Scrapper,name ='scrapper') ,
   url( r'^clear/$', views.clear_db,name ='clear_db') ,
   url( r'^algo/$', views.Algorithm,name ='algo') ,
   url( r'^build/(?P<id>\d+)/$', views.Build_Pc,name ='build') ,
   url( r'^add_to_fav/(?P<id>\d+)/$', views.Add_Fav,name ='add_to_fav') ,
   url( r'^view_fav/$', views.View_Fav , name ='view_fav') ,
   url( r'^register/$', views.Register,name ='register') ,
   url( r'^logout/$', views.Logout,name ='logout') ,
   url( r'^recent_buys/$', views.Recent,name ='recent') ,
   url( r'^del_fav/(?P<id>\d+)/$', views.Delete_Fav,name ='del_fav') ,
   url( r'^del_ref/(?P<id>\d+)/$', views.Delete_Ref,name ='del_ref') ,
   url( r'^refer/(?P<id>\d+)/$', views.Refer,name ='refer') ,
   url( r'^view_ref/$', views.View_Ref , name ='view_ref') ,
# 
]
