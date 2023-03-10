from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView

app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agent_list"),
    path("form_agent", AgentCreateView.as_view(), name="agent_form"),
    path('<int:pk>/', AgentDetailView.as_view(), name="agent_detail"),
    # path('<int:pk>/update', AgentUpdateView.as_view(), name="agent_update"),
    # path('<int:pk>/delete', AgentDeleteView.as_view(), name="agent_delete"),
    
]