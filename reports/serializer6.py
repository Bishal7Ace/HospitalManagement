from rest_framework import serializers
from .models import *
from staffandpatient.serializer2 import PatientName

class WholePatientsDemographicReportSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=WholePatientsDemographicsReport

class WholeAppointmentReportSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=WholeAppointmentReport

class PatientDemographicsSerializer(serializers.ModelSerializer):
    patient_name=PatientName()
    class Meta:
         fields="__all__"
         model=PatientDemographics
class AppointmentSerializer(serializers.ModelSerializer):
    patient_name=PatientName()
    class Meta:
         fields="__all__"
         model=AppointmentReport
class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Expense
class RevenueSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=RevenueReport