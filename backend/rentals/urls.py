from django.urls import path
from rentals.views import list_view, create_view, confirm_rental_view

urlpatterns = [
    path("", list_view, name="rentals"),
    path("create-new-rental/product/<int:pk>/", create_view, name="new-rental"),
    path("confirm-rental/<int:pk>/", confirm_rental_view, name="confirm-rental"),
]