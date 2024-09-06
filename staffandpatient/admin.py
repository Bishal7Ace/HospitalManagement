from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Customer)
# admin.site.register(Order)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    pass