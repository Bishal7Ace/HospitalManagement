from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns=[
    path('emergency',EmergencySituationApi.as_view()),
    path('emergencyId/<pk>',EmergencySituationIdApi.as_view()),
    path('patienttriage',PatientTriageApi.as_view()),
    path("patienttriageId/<pk>",PatientTriageIdApi.as_view()),
]