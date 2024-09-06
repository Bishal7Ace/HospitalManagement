from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from .serializer7 import *
from core.permissions import CustomModelPermission

class InvoiceApi(generics.ListCreateAPIView):
    queryset_model=Invoice
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=InvoiceSerializer
    queryset=Invoice.objects.all()

class InvoiceIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Invoice
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=InvoiceSerializer
    queryset=Invoice.objects.all()

