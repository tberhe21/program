# all classes in this file represent a data model in the application with data type validation
# ctrl click to view Django package codes
from django.db import models


class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True, editable=False)
    patient_fname = models.CharField(max_length=50)
    patient_lname = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=10)
    patient_addr = models.CharField(max_length=100)
    patient_number = models.CharField(max_length=20)

# the code below or "class Meta" specifies or configers the database table for this model
    class Meta:
        db_table = 'patients'


class Conditions(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=150)

    class Meta:
        db_table = 'conditions'


class Medications(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=100)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE)

    class Meta:
        db_table = 'medications'

# these models are used to store and manage data related to the class name mentioned

# foreign key relationships


class PatientCondition(models.Model):
    # defines a foreign relationship with Patients modeland this creates links
    # between two tables in the database that would be the PatientCondition instance having reference to the Patients table
    # the same applies to PatientMedications class
    patient = models.ForeignKey(
        Patients, on_delete=models.CASCADE, db_column='patient_id', primary_key=True)
    condition = models.ForeignKey(
        Conditions, on_delete=models.CASCADE)

    class Meta:
        db_table = 'patientcondition'
        unique_together = (('patient', 'condition'))


class PatientMedications(models.Model):
    patient = models.ForeignKey(
        Patients, on_delete=models.CASCADE, db_column='patient_id', primary_key=True)
    medication = models.ForeignKey(Medications, on_delete=models.CASCADE)

    class Meta:
        db_table = 'patientmedications'
        unique_together = (('patient', 'medication'))


class CareAssociations(models.Model):
    care_association_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    professional_id = models.IntegerField()


# audit.log
