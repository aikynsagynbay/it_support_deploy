from django.urls import path
from . import views

urlpatterns = [
    path("", views.ticket_list, name="ticket_list"),
    path("status/<int:pk>/", views.update_status, name="update_status"),
    path("delete/<int:pk>/", views.delete_ticket, name="delete_ticket"),
]
