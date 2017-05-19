from django.db import models
import datetime

# Create your models here.


class CheatApplication(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    class_size = models.IntegerField(default=0)
    num_q = models.IntegerField(default=0)
    date_occurred = models.DateTimeField

