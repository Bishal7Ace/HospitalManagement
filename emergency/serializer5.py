from rest_framework import serializers
from .models import *

class EmergencySituationSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=EmergencySituation


class PatientTriageSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=PatientTriage