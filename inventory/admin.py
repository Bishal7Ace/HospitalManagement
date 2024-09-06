from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Customer)
# admin.site.register(Order)


@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    pass
@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    pass
@admin.register(InventoryTrack)
class Inventorytrack(admin.ModelAdmin):
    pass