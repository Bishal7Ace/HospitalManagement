from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Customer)
# admin.site.register(Order)


@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    pass

