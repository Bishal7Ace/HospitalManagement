from django.db import models
from staffandpatient.models import Patient
# Create your models here.
class ElectronicHealthRecord(models.Model):
    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE)
    medical_history = models.TextField(null=True,blank=True)
    diagnosis = models.TextField(null=True,blank=True)
    medications = models.TextField(null=True,blank=True)
    treatment_plan = models.TextField(null=True,blank=True)
    appointment_history = models.TextField(null=True,blank=True)
    billing_info = models.TextField(null=True,blank=True)
    insurance_info = models.TextField(null=True,blank=True)
    
  