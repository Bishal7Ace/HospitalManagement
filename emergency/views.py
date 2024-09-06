from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework import status
from .serializer5 import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.permissions import CustomModelPermission
# from django_filters.rest_framework import DjangoFilterBackend?
from rest_framework import filters

class EmergencySituationApi(generics.ListCreateAPIView):
    queryset=EmergencySituation.objects.all()
    serializer_class=EmergencySituationSerializer

class EmergencySituationIdApi(generics.RetrieveDestroyAPIView):
    queryset=EmergencySituation.objects.all()
    serializer_class=EmergencySituationSerializer

class PatientTriageApi(generics.ListCreateAPIView):
    queryset=PatientTriage.objects.all()
    serializer_class=PatientTriageSerializer
class PatientTriageIdApi(generics.RetrieveDestroyAPIView):
    queryset=PatientTriage.objects.all()
    serializer_class=PatientTriageSerializer