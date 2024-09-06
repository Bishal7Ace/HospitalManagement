from django.db import models
from django.utils import timezone
# Create your models here.
level=[('Immediate','Immediate'),('Delayed','Delayed'),('Minor','Minor')]

class EmergencySituation(models.Model):
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

class PatientTriage(models.Model):
    patient_name = models.CharField(max_length=100)
    emergency_situation = models.ForeignKey(EmergencySituation, on_delete=models.CASCADE)
    triage_level = models.CharField(max_length=200,choices=level,default='Immediate')  # Triage level: e.g., "Immediate", "Delayed", "Minor", etc.
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Triage for {self.patient_name}"
