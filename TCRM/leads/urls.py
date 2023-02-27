from django.urls import path
from .views import homepage


app_name = "leads"


urlpatterns = [
    path('', homepage, name="homepage"),

]