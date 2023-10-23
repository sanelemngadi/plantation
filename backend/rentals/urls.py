from django.urls import path
from rentals import views

urlpatterns = [
    path("", views.rental_list_view, name="rentals"),
    path("create-new-rental/product/<int:pk>/", views.rental_create_view, name="new-rental"),
    path("confirm-rental/<int:pk>/", views.confirm_rental_view, name="confirm-rental"),
    path("item/<int:pk>/", views.rental_detail_view, name="rental-detail"),
]