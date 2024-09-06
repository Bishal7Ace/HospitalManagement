from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Customer)
# admin.site.register(Order)


@admin.register(EmergencySituation)
class EmergencySituation(admin.ModelAdmin):
    pass

@admin.register(PatientTriage)
class PateintTriage(admin.ModelAdmin):
    pass