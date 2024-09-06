from django.db import models
from core.models import User

# Create your models here.
from django.utils import timezone
type=[('male','male'),('female','female'),('other','other')]

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    medical_history = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    prefered_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True,blank=True)
    age=models.PositiveIntegerField()
    sex=models.CharField(max_length=300,choices=type)
    

    def __str__(self):
        return self.name

class Schedule(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=100)
    prefered_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)



class Appointment(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prefered_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name}'s Appointment with Dr. {self.prefered_doctor} on {self.appointment_date} at {self.appointment_time}"


class AppointmentRequest(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    CANCELED = 'denied' 
    choices=[('denied','denied'),('approved','approved'),('pending','pending')]
    patient_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    prefered_doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=200,choices=choices,default='pending')
    email=models.EmailField()
    

    def __str__(self):
        return f"Appointment Request by {self.patient_name}" 
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=AppointmentRequest)
def appointment_re(sender, instance, **kwargs):
    
    if instance.status =='denied':
        send_low_inventory_email(instance)
    elif instance.status =='approved':
        low_inventory_email(instance)

def send_low_inventory_email(appointmentreq):
    subject = f"about your appointment request {appointmentreq.patient_name}"
    message = f"your appointment with Dr.{appointmentreq.prefered_doctor} has been denied"
    # user_email = appointmentreq.user.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [appointmentreq.email])
def low_inventory_email(appointmentreq):
    subject = f"about your appointment request {appointmentreq.patient_name}"
    message = f"your appointment with Dr.{appointmentreq.prefered_doctor} has been approved"
    # user_email = appointmentreq.user.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [appointmentreq.email])
