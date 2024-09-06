
from .views import *
from django.urls import path
from django.contrib import admin


urlpatterns=[
    path('wholeapp',WholeAppointmentApi.as_view()),
    path('wholeappId/<pk>',WholeAppointmentIdApi.as_view()),
    path('wholepati',WholePatientsDemographicsReporApi.as_view()),
    path('wholepatiId/<pk>',WholePatientsDemographicsReportIdApi.as_view()),
    path('expense',ExpenseApi.as_view()),
    path('expenseId/<pk>',ExpenseIdApi.as_view()),
    path('revenue',RevenueApi.as_view()),
    path('revenueId/<pk>',RevenueIdApi.as_view()),
    path('appointment',AppointmentApi.as_view()),
    path('appointmentId/<pk>',AppointmentIdApi.as_view()),
    path('patientdemo',PatientDemographicsApi.as_view()),
    path('patientdemoId/<pk>',PatientDemographicsIdApi.as_view()),
   
    
]