from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns=[
    path('electronichealthrecord',ElectronicHealthRecordApi.as_view()),
    path('electronichealthrecordId/<pk>',ElectronicHealthRecordIdApi.as_view()),
]