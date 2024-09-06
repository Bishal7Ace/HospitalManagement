from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Customer)
# admin.site.register(Order)


@admin.register(WholeAppointmentReport)
class WholeAppointmentReportAdmin(admin.ModelAdmin):
    pass

@admin.register(WholePatientsDemographicsReport)
class WholePatientsDemographicsReportAdmin(admin.ModelAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass

@admin.register(RevenueReport)
class RevenueReportAdmin(admin.ModelAdmin):
    pass

@admin.register(AppointmentReport)
class AppointmentReportAdmin(admin.ModelAdmin):
    pass

@admin.register(PatientDemographics)
class PatientDemographicsAdmin(admin.ModelAdmin):
    pass