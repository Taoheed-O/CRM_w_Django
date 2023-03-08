from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Lead, Agent
from .forms import LeadForm, CustomerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomerForm

    def get_success_url(self):
        return reverse("login")

# CLASS BASED VIEW FOR HOMEPAGE
# class HomePage(TemplateView):
#     template_name = "leads/homepage.html"


# FUNCTION BASED VIEW FOR HOMEPAGE
def homepage(request):
    return render(request, 'leads/homepage_lead.html')


# CLASS BASED VIEW FOR DETAILS VIEW
# class LeadDetailsView(DetailView):
#     template_name = "leaddetails.html"
#     queryset = Lead.objects.all()
#     context_object_name = "details"


# FUNCTION BASED VIEW FOR DETAILS VIEW
@login_required(login_url='/login')
def lead_details(request, pk):
    details = Lead.objects.get(id=pk)
    context = {"details": details}
    return render(request, 'leaddetails.html', context)


# class LeadListView(ListView):
#     template_name = "leadlist.html"
#     queryset = Lead.objects.all()
#     context_object_name = "leads"


@login_required(login_url='/login')
def lead_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, 'leadlist.html', context)


# class LeadCreateView(CreateView):
#     template_name = "lead_form.html"
#     lead_form = LeadForm
#
#     def get_success_url(self):
#         return reverse("leadlist")


@login_required(login_url='/login')
def lead_form(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        subject = "Welcome to TCRM."
        message = f"Hi , you are now a lead at TCRM."
        email_from = "oyeniyiemperor@gmail.com"
        recipient_list = ["oyeniyiemperor@gmail.com"]
        if form.is_valid():
            send_mail(subject, message, email_from, recipient_list)
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'lead_form.html', context)


@login_required(login_url='/login')
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leadlist')
    context = {"form": form,
               "lead": lead}
    return render(request, 'lead_update.html', context)


@login_required(login_url='/login')
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')
