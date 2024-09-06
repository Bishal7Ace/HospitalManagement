# Generated by Django 5.0.3 on 2024-03-10 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('staffandpatient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevenueReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('lab_test_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('imaging_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('medication_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WholeAppointmentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_appointments', models.PositiveIntegerField()),
                ('appointment_types_distribution', models.JSONField()),
                ('appointment_status_distribution', models.JSONField()),
                ('provider_distribution', models.JSONField()),
                ('location_distribution', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='WholePatientsDemographicsReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_patients', models.IntegerField(default=0)),
                ('age_0_18', models.IntegerField(default=0)),
                ('age_19_35', models.IntegerField(default=0)),
                ('age_36_50', models.IntegerField(default=0)),
                ('age_51_65', models.IntegerField(default=0)),
                ('age_66_plus', models.IntegerField(default=0)),
                ('male_patients', models.IntegerField(default=0)),
                ('female_patients', models.IntegerField(default=0)),
                ('other_gender_patients', models.IntegerField(default=0)),
                ('ethnicity_counts', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date_time', models.DateTimeField()),
                ('appointment_type', models.CharField(choices=[('Consultation', 'Consultation'), ('Follow-up', 'Follow-up'), ('Procedure', 'Procedure'), ('Screening', 'Screening'), ('Vaccination', 'Vaccination')], max_length=20)),
                ('appointment_duration', models.IntegerField()),
                ('reason_for_appointment', models.TextField()),
                ('appointment_referral_source', models.CharField(max_length=100)),
                ('appointment_cancellation_reason', models.TextField(blank=True)),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffandpatient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Personnel', 'Personnel expenses'), ('Supplies', 'Supplies and equipment expenses'), ('Facility', 'Facility and overhead expenses'), ('Administrative', 'Administrative expenses'), ('Depreciation', 'Depreciation and amortization expenses'), ('Other', 'Other expenses')], max_length=50)),
                ('payment_date', models.DateField()),
                ('expense_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDemographics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('ethnicity', models.CharField(choices=[('White', 'White'), ('Black or African American', 'Black or African American'), ('Asian', 'Asian'), ('Hispanic or Latino', 'Hispanic or Latino'), ('Other', 'Other')], max_length=50)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=20)),
                ('employment_status', models.CharField(choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Retired', 'Retired'), ('Other', 'Other')], max_length=20)),
                ('primary_language', models.CharField(max_length=50)),
                ('insurance_coverage', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffandpatient.patient')),
            ],
        ),
    ]