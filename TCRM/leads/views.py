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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(first_name=first_name,
                                last_name=last_name,
                                age=age,
                                agent=agent)
            return redirect('/')
    context = {"form":form}
    return render(request,'lead_form.html',context)