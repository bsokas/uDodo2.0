from django.shortcuts import render
from django.http import HttpResponse

def initial_view(request):
    return HttpResponse("This will be the home page.")
