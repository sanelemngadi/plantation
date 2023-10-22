from django.urls import path
from notifications import views

urlpatterns = [
    path("", views.notification_list_view, name="notifications")
]
