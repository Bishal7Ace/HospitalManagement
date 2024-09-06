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
from .serializer1 import *
from core.permissions import CustomModelPermission

class SupplierApi(generics.ListCreateAPIView):
    queryset_model=Supplier
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=SupplierSerializer
    queryset=Supplier.objects.all()

class SupplierIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Supplier
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=SupplierSerializer
    queryset=Supplier.objects.all()

class InventoryApi(generics.ListCreateAPIView):
    queryset_model=Inventory
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=InventorySerializer
    queryset=Inventory.objects.all()

class InventoryIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Inventory
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=InventorySerializer
    queryset=Inventory.objects.all()


class InventoryTrackApi(generics.ListCreateAPIView):
    queryset_model=InventoryTrack
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=InventoryTrack
    queryset=InventoryTrack.objects.all()

class InventoryTrackIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=InventoryTrack
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=InventoryTrack
    queryset=InventoryTrack.objects.all()


