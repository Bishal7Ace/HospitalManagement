from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission, IsAuthenticatedOrReadOnly
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework import generics,permissions
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from core.permissions import CustomModelPermission
from .serializer2 import *
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class DoctorApi(generics.ListCreateAPIView):
    queryset_model=Doctor
    permission_classes=[IsAuthenticatedOrReadOnly,CustomModelPermission]
    serializer_class=DoctorSerializer
    queryset=Doctor.objects.all()
    

class DoctorIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Doctor
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=DoctorSerializer
    queryset=Doctor.objects.all()

class StaffmemberApi(generics.ListCreateAPIView):
    queryset_model=StaffMember
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=StaffSerializer
    queryset=StaffMember.objects.all()

class StaffmemberIDApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=StaffMember
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=StaffSerializer
    queryset=StaffMember.objects.all()

class ScheduleApi(generics.ListCreateAPIView):
    queryset_model=Schedule
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ScheduleSerializer
    queryset=Schedule.objects.all()

class ScheduleIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Schedule
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=ScheduleSerializer
    queryset=Schedule.objects.all()

class PatientApi(generics.ListCreateAPIView):
    filterset_fields=['name']
    search_fields=['contact_info']
    
    queryset_model=Patient
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=PatientSerializer
    queryset=Patient.objects.all()

class PatientIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Patient
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=PatientSerializer
    queryset=Patient.objects.all()

class AppointmentApi(generics.ListCreateAPIView):
    queryset_model=Appointment
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=AppointmentSerializer
    queryset=Appointment.objects.all()

class AppointmentIdApi(generics.RetrieveUpdateDestroyAPIView):
    queryset_model=Appointment
    permission_classes=[IsAuthenticated,CustomModelPermission]
    serializer_class=AppointmentSerializer
    queryset=Appointment.objects.all()

class AppointmentRequestApi(generics.ListCreateAPIView):

    queryset_model=AppointmentRequest
    permission_classes=[IsAuthenticated,CustomModelPermission]
    filterset_fields=['patient_name']
    search_fields=['contact_info']
    
    serializer_class=AppointmentRequestSerializer
    queryset=AppointmentRequest.objects.all()
   




class AppointmentReApi(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated,CustomModelPermission]
    queryset_model=AppointmentRequest
    serializer_class=AppointmentRequestSerializer
    queryset=AppointmentRequest.objects.all()

# # views.py
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from .models import AppointmentRequest
# from .serializers import AppointmentRequestSerializer




# class PendingAppointmentRequestsAPIView(generics.ListAPIView):
#     # permission_classes=[IsAuthenticated,CustomModelPermission]
#     queryset_model=AppointmentRequest
#     queryset=AppointmentRequest.objects.all()
#     serializer_class = AppointmentRequestSerializer
#     # group_required = 'Staff'

#     # def list(self, request, *args, **kwargs):
#     #     # Check if user is in the required group
#     #     if not request.user.groups.filter(name=self.group_required).exists():
#     #         return Response("Permission denied", status=status.HTTP_403_FORBIDDEN)
        
#     #     # Your view logic here
#     #     return Response("Your data", status=status.HTTP_200_OK)
#     # def get_queryset(self):
#     #         # Retrieve all pending appointment requests
#     #         return AppointmentRequest.objects.filter(status=AppointmentRequest.PENDING)
        
   
    
#     group_required = 'Staff'
#     custom_permission_codename = 'can_view_custom_data'

#     def get_queryset(self):
#         # Your custom queryset logic here
#         return []

#     def list(self, request, *args, **kwargs):
#         # Check if the user is in the required group
#         if not request.user.groups.filter(name=self.group_required).exists():
#             return Response("Permission denied", status=status.HTTP_403_FORBIDDEN)

#         # Check if the user has the required custom permission
#         if not request.user.has_perm(f'yourapp.{self.custom_permission_codename}'):
#             return Response("Permission denied", status=status.HTTP_403_FORBIDDEN)
        
#         def get_queryset(self):
#     #         # Retrieve all pending appointment requests
#             return AppointmentRequest.objects.filter(status=AppointmentRequest.PENDING)
        
#         return super().list(request, *args, **kwargs)
    
   
# class ApprovedAppointmentRequestsAPIView(generics.UpdateAPIView):
#     queryset=AppointmentRequest.objects.all()

#     serializer_class = AppointmentRequestSerializer
#     queryset_model=AppointmentRequest
      

   
#     def get_queryset(self):
#             return AppointmentRequest.objects.all()
#     def update(self, request, *args, **kwargs):
#             appointment_request = self.get_object()
#             appointment_request.status = AppointmentRequest.APPROVED
#             appointment_request.save()
#             return Response(self.get_serializer(appointment_request).data, status=status.HTTP_200_OK)
# class CanceledApointmentRequestApi(generics.UpdateAPIView):
#     queryset_model=AppointmentRequest
#     serializer_class = AppointmentRequestSerializer
#     # permission_classes = [IsAuthenticated,CustomModelPermission]  # Ensure only authenticated doctors can access
#     def get_queryset(self):
#         return AppointmentRequest.objects.all()
    
#     def update(self, request, *args, **kwargs):
#         appointment_request = self.get_object()
#         appointment_request.status = AppointmentRequest.CANCELED
#         appointment_request.save()
#         return Response(self.get_serializer(appointment_request).data, status=status.HTTP_200_OK)
    

