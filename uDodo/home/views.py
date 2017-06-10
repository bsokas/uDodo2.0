from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("This will be the home page.")
    return render(request, "uDodo_home.html")
