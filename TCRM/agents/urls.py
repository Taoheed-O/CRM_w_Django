from django.urls import path
from .views import AgentListView, AgentCreateView

app_name = "agents"

urlpatterns = [
    path("", AgentListView.as_view(), name="agent_list"),
    path("form_agent", AgentCreateView.as_view(), name="agent_form")

]