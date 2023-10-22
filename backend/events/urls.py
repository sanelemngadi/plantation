from django.urls import path
from events.views import list_view, create_view

urlpatterns = [
    path("", list_view, name="events"),
    path("create-new/", create_view, name="new-event"),
]