from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Invoice
# from staffandpatient.models import AppointmentReque
# from Accounting.models import Reservation
from staffandpatient.models import Patient
from django.core.mail import send_mail
@receiver(post_save,sender = Patient)
def invoice_create(sender,instance,*args, **kwargs):
    print(instance)
    if Invoice.objects.filter(patient_name=instance).exists():
        pass
    else:
        price=500
        Invoice.objects.create(

            patient_name = instance, 
            price=price
            
             
            
           
        )
        # invoice = Invoice.objects.filter(reservation = instance).first()
#
            
            
             
            
           