from .models import *
from rest_framework import serializers
from staffandpatient.serializer2 import PatientName


class InvoiceSerializer(serializers.ModelSerializer):
    patient_name=PatientName()
    class Meta:
         fields="__all__"
         model=Invoice

