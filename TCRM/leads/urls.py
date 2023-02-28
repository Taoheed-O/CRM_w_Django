from django.urls import path
from .views import homepage, lead_details


app_name = "leads"


urlpatterns = [
    path('', homepage, name="homepage"),
    path('<int:pk>/', lead_details, name="lead_details"),

]