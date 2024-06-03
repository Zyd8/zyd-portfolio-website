from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.iot, name="iot"),
    path('post_pc_case_temp_humidity/', views.post_pc_case_temp_humidity, name='post_pc_case_temp_humidity')
]