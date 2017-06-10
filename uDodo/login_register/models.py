from django.db import models
from django.contrib.auth.models import User

#User registration stores a site visitor's registration
#It acts as a data-holding table for processing and validation of an applicant
class UserApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=70)
    other_name = models.CharField(max_length=20, null=True, blank=True)
    #institution = #will probably use a choices file here

#User profile holds the registration details of an actual user
#An entry in the UserProfile table reflects a validated user
class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
