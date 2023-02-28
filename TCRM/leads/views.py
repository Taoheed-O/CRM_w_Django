from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm

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


def lead_form(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form":form}
    return render(request,'lead_form.html',context)



def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form":form,
               "lead":lead}
    return render(request, 'lead_update.html', context)



def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')