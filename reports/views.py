from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *

from rest_framework import generics

from .serializer6 import *
from core.permissions import CustomModelPermission


class WholeAppointmentApi(generics.ListCreateAPIView):
    queryset_model=WholeAppointmentReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=WholeAppointmentReportSerializer
    queryset=WholeAppointmentReport.objects.all()


class WholeAppointmentIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=WholeAppointmentReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=WholeAppointmentReportSerializer
    queryset=WholeAppointmentReport.objects.all()

class WholePatientsDemographicsReporApi(generics.ListCreateAPIView):
    queryset_model=WholePatientsDemographicsReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=WholePatientsDemographicReportSerializer
    queryset=WholePatientsDemographicsReport.objects.all()

class WholePatientsDemographicsReportIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=WholePatientsDemographicsReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=WholePatientsDemographicReportSerializer
    queryset=WholePatientsDemographicsReport.objects.all()



class AppointmentApi(generics.ListCreateAPIView):
    queryset_model=AppointmentReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=AppointmentSerializer
    queryset=AppointmentReport.objects.all()

class AppointmentIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=AppointmentReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=AppointmentSerializer
    queryset=AppointmentReport.objects.all()


class PatientDemographicsApi(generics.ListCreateAPIView):
    queryset_model=PatientDemographics
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=PatientDemographicsSerializer
    queryset=PatientDemographics.objects.all()

class PatientDemographicsIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=PatientDemographics
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=PatientDemographicsSerializer
    queryset=PatientDemographics.objects.all()

class ExpenseApi(generics.ListCreateAPIView):
    queryset_model=Expense
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ExpenseSerializer
    queryset=Expense.objects.all()

class ExpenseIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Expense
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ExpenseSerializer
    queryset=Expense.objects.all()

class RevenueApi(generics.ListCreateAPIView):
    queryset_model=RevenueReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=RevenueSerializer
    queryset=RevenueReport.objects.all()

class RevenueIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=RevenueReport
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=RevenueSerializer
    queryset=RevenueReport.objects.all()