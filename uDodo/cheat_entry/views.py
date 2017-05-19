from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import CheatApplicationForm

# Create your views here.

def home(request):

    new_form = CheatApplicationForm()
    context = {

        'form': new_form,
    }

    return render(request, 'CheatEntryApplication.html', context)

def submission(request):

    if request.method=="POST":

        new_form = CheatApplicationForm(request.POST)
        new_form.save()

        return HttpResponse("Thank you for your submission")

    return HttpResponse("There was a problem with your submission")

