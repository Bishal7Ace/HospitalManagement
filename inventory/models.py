from django.db import models
choices=[('medical supplies','medical supplies'),('medical equipment','medical equipment'),('medications','medications')]

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=300)
    contact=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    name=models.CharField(max_length=300)
    category=models.CharField(max_length=200,choices=choices)
    description=models.TextField()
    supplier=models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class InventoryTrack(models.Model):
    name=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    quantity_available=models.IntegerField()
    low_inventory_threshold = models.IntegerField(default=10)
    unit_price=models.IntegerField()
    total_price=models.IntegerField()
    notes=models.TextField(null=True,blank=True)
    product_in=models.IntegerField(null=True,blank=True)
    opening_numbers_of_product=models.IntegerField(null=True,blank=True)
    closing_number_of_products=models.IntegerField(null=True,blank=True)
    supplier=models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
    # def __str__(self):
    #     return self.name
    
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=InventoryTrack)
def check_inventory(sender, instance, **kwargs):
    
    if instance.quantity_available < instance.low_inventory_threshold:
        send_low_inventory_email(instance)

def send_low_inventory_email(inventoryTrack):
    subject = f"Low Inventory Alert: {inventoryTrack.name}"
    message = f"The quantity of {inventoryTrack.name} is running low. Please restock."
    supplier_email = inventoryTrack.supplier.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [supplier_email])
