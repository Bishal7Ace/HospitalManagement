from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *

from rest_framework import generics

from .serializer4 import *
from core.permissions import CustomModelPermission


class ElectronicHealthRecordApi(generics.ListCreateAPIView):
    queryset_model=ElectronicHealthRecord
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ElectronicHealthRecordSerializer
    queryset=ElectronicHealthRecord.objects.all()
class ElectronicHealthRecordIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=ElectronicHealthRecord
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ElectronicHealthRecordSerializer
    queryset=ElectronicHealthRecord.objects.all()
