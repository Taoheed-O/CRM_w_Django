from django.urls import path
from .views import homepage, lead_details, lead_form


app_name = "leads"


urlpatterns = [
    path('', homepage, name="homepage"),
    path('form/', lead_form, name="lead_form" ),
    path('<int:pk>/', lead_details, name="lead_details"),

]