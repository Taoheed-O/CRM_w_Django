from django.urls import path
from .views import (HomePage, lead_form,
    lead_update, lead_delete, lead_details, LeadListView)


app_name = "leads"


urlpatterns = [
    path('', HomePage.as_view(), name="homepage"),
    path('leadlist/', LeadListView.as_view(), name="leadlist"),
    path('form/', lead_form, name="lead_form"),
    path('<int:pk>/update', lead_update, name="lead_update"),
    path('<int:pk>/delete', lead_delete, name="lead_delete"),
    path('<int:pk>/', lead_details, name="lead_details"),

]
