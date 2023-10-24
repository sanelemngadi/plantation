from django.urls import path
from suppliers import views

urlpatterns = [
    path("", views.supplier_list_view, name="suppliers"),
    path("create/", views.supplier_create_view, name="supplier-create"),
    path("update/<int:pk>/", views.supplier_update_view, name="supplier-update"),
    path("remove/<int:pk>/", views.supplier_remove_view, name="supplier-remove"),
]