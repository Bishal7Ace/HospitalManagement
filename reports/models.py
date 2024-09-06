from django.db import models
from staffandpatient.models import Patient
from inventory.models import Supplier

from django.db import models

class WholePatientsDemographicsReport(models.Model):
    # Total number of patients
    total_patients = models.IntegerField(default=0)

    # Age distribution
    age_0_18 = models.IntegerField(default=0)  # Number of patients aged 0-18
    age_19_35 = models.IntegerField(default=0)  # Number of patients aged 19-35
    age_36_50 = models.IntegerField(default=0)  # Number of patients aged 36-50
    age_51_65 = models.IntegerField(default=0)  # Number of patients aged 51-65
    age_66_plus = models.IntegerField(default=0)  # Number of patients aged 66 and above

    # Gender distribution
    male_patients = models.IntegerField(default=0)
    female_patients = models.IntegerField(default=0)
    other_gender_patients = models.IntegerField(default=0)
    ethnicity_counts = models.JSONField(default=dict)




class WholeAppointmentReport(models.Model):
    # Total number of appointments
    total_appointments = models.PositiveIntegerField()

    # Appointment type distribution
    appointment_types_distribution = models.JSONField()

    # Appointment status distribution
    appointment_status_distribution = models.JSONField()

    # Provider distribution
    provider_distribution = models.JSONField()

    # Location distribution
    location_distribution = models.JSONField()

   


class PatientDemographics(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ETHNICITY_CHOICES = [
        ('White', 'White'),
        ('Black or African American', 'Black or African American'),
        ('Asian', 'Asian'),
        ('Hispanic or Latino', 'Hispanic or Latino'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Retired', 'Retired'),
        ('Other', 'Other'),
    ]

    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    ethnicity = models.CharField(max_length=50, choices=ETHNICITY_CHOICES)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS_CHOICES)
    primary_language = models.CharField(max_length=50)
    insurance_coverage = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
   

    



class AppointmentReport(models.Model):

    APPOINTMENT_TYPE_CHOICES = [
        ('Consultation', 'Consultation'),
        ('Follow-up', 'Follow-up'),
        ('Procedure', 'Procedure'),
        ('Screening', 'Screening'),
        ('Vaccination', 'Vaccination'),
    ]

    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointment_date_time = models.DateTimeField()
    
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPE_CHOICES)
    appointment_duration = models.IntegerField()  # Duration in minutes
    reason_for_appointment = models.TextField()
    appointment_referral_source = models.CharField(max_length=100)
    appointment_cancellation_reason = models.TextField(blank=True)
    # Additional fields if needed


    def __str__(self):
        return f"Appointment for {self.patient_name} on {self.appointment_date_time}"


class RevenueReport(models.Model):

    consultation_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lab_test_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imaging_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    medication_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   

CATEGORY_CHOICES = [
        ('Personnel', 'Personnel expenses'),
        ('Supplies', 'Supplies and equipment expenses'),
        ('Facility', 'Facility and overhead expenses'),
        ('Administrative', 'Administrative expenses'),
        ('Depreciation', 'Depreciation and amortization expenses'),
        ('Other', 'Other expenses'),
    ]
class Expense(models.Model):
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)

    # Vendor information
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    
    payment_date = models.DateField()
     # Expense date
    expense_date = models.DateField()


    # Amount
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

   