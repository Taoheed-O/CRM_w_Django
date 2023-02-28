from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead

# Create your views here.


def homepage(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, 'leads/homepage.html', context)


def lead_details(request, pk):
    details = Lead.objects.get(id=pk)
    context = {"details":details}
    return render(request, 'leadlist.html', context)