from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns=[
    path('doctors',DoctorApi.as_view()),
    path('doctorsId/<pk>',DoctorIdApi.as_view()),
    path('staffs',StaffmemberApi.as_view()),
    path("staffsId/<pk>",StaffmemberIDApi.as_view()),
    path('schedule',ScheduleApi.as_view()),
    path('scheduleId/<pk>',ScheduleIdApi.as_view()),
    path('patient',PatientApi.as_view()),
    path('patientId/<pk>',PatientIdApi.as_view()),
    path('appointment',AppointmentApi.as_view()),
    path('appointmentId/<pk>',AppointmentIdApi.as_view()),
    path('appointmentrequest',AppointmentRequestApi.as_view()),
    # path('acceptreq/<pk>',ApprovedAppointmentRequestsAPIView.as_view()),
    # path('pendingreq',PendingAppointmentRequestsAPIView.as_view()),
    # path('cancelreq/<pk>',CanceledApointmentRequestApi.as_view()),
    path('a/<pk>',AppointmentReApi.as_view()),

]
