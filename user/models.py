from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class StudentEnroll(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    occupation = models.CharField(max_length=300)
    qualification = models.CharField(max_length=300)
    course = models.CharField(max_length=300)
    batch = models.CharField(max_length=300)
    

class Contact_form_tabledahanraj(models.Model):
   fullname = models.CharField(max_length=500)
   mobile = models.CharField(max_length=500)
   email = models.CharField(max_length=500)
   course = models.CharField(max_length=500)
   mess = models.CharField(max_length=500)
   status = models.CharField(max_length=20, default="Pending")


class Contact_callbackdahanraj(models.Model):
   cb_name = models.CharField(max_length=500)
   cb_mobile = models.CharField(max_length=500)
   cb_time = models.CharField(max_length=100)
   status = models.CharField(max_length=20, default="Pending")
   
