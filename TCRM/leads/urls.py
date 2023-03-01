from django.urls import path
from .views import homepage, lead_details, lead_form, lead_update, lead_delete


app_name = "leads"


urlpatterns = [
    path('', homepage, name="homepage"),
    path('form/', lead_form, name="lead_form" ),
    path('<int:pk>/update', lead_update, name="lead_update"),
    path('<int:pk>/delete', lead_delete, name="lead_delete"),
    path('<int:pk>/', lead_details, name="lead_details"),

]