from .views import *
from django.urls import path

urlpatterns=[
    
    path('invoice',InvoiceApi.as_view()),
    path('invoiceId/<pk>',InvoiceIdApi.as_view()),

]