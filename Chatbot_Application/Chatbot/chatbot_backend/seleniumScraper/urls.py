from django.urls import path
from django.contrib import admin
from django.urls import path, include
#now import the views.py file into this code
from . import views
urlpatterns=[
    path('', views.view_name, name="view_name"),
    path('',views.index, name='index')
]