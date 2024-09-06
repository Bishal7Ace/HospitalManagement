from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns=[
    path('suppliers',SupplierApi.as_view()),
    path('suppliersId/<pk>',SupplierIdApi.as_view()),
    path('inventory',InventoryApi.as_view()),
    path("inventoryId/<pk>",InventoryIdApi.as_view()),
    path('inventorytrack',InventoryTrackApi.as_view()),
    path('inventorytrack',InventoryTrackIdApi.as_view()),
]