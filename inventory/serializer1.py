from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Supplier


class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=Inventory


class InventorytrackSerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model=InventoryTrack