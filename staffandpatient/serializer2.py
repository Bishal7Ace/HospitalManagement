from rest_framework import serializers
from .models import *

class PatientName(serializers.RelatedField):
    queryset=Patient.objects.all()
    def to_representation(self, value):
        return value.name
    def to_internal_value(self, data):
        name,_=Patient.objects.get_or_create(name=data)
        return name
    
class DoctorName(serializers.RelatedField):
    queryset=Doctor.objects.all()
    def to_representation(self, value):
        return value.name
    def to_internal_value(self, data):
        prefered_doctor,_=Doctor.objects.get_or_create(name=data)
        return prefered_doctor

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Doctor

class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=StaffMember


class ScheduleSerializer(serializers.ModelSerializer):
    patient_name=PatientName()
    prefered_doctor=DoctorName()
    class Meta:
         fields="__all__"
         model=Schedule


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Patient


class AppointmentSerializer(serializers.ModelSerializer):
    patient_name=PatientName()
    prefered_doctor=DoctorName()
    class Meta:
         fields="__all__"
         model=Appointment


class AppointmentRequestSerializer(serializers.ModelSerializer):
    prefered_doctor=DoctorName()
    class Meta:
         fields="__all__"
         model=AppointmentRequest