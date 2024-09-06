from rest_framework import serializers
from .models import *
from staffandpatient.serializer2 import PatientName

class ElectronicHealthRecordSerializer(serializers.ModelSerializer):
    patient_name=PatientName()
    class Meta:
         model=ElectronicHealthRecord
         fields= "__all__"
