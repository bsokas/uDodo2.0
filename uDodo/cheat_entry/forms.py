'''
The form in this file connects to the cheat application table
'''

from django import forms
from django.forms import ModelForm
from .models import CheatApplication
from django.forms.extras.widgets import SelectDateWidget

import datetime

class CheatApplicationForm(forms.Form):

    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    class_size = forms.IntegerField(required=True)
    number_of_questions = forms.IntegerField(required=True)
    date_occurred = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = CheatApplication
        fields = ['name', 'subject', 'class_size', 'num_q', 'date_occurred']
