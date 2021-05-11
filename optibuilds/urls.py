
from django.contrib import admin
from django.urls import path , include
from System.urls import *

urlpatterns = [
    path('' , include('System.urls') ),
    path('admin/', admin.site.urls),
]