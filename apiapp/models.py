# models.py
from django.db import models
from django.db import models
from phone_field import PhoneField

# Create your models here.
class Event(models.Model):
    company_name = models.CharField(max_length=250)
    date  = models.DateField()
    date_to_start  = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
    street_address = models.CharField(max_length=50)
    fax_number = PhoneField(null=False, blank=False, unique=True)
    phone_number =  PhoneField(null=False, blank=False, unique=True)
    department_Location = models.CharField(max_length=50)
    project_name = models.CharField(max_length=250)
    company_address = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.project_name


