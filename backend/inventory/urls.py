from django.urls import path
from inventory import views

urlpatterns = [
    path("", views.inventory_view, name="inventory"),
    path("row/", views.row_create_view, name="row-create"),
    path("shelf/", views.shelf_create_view, name="shelf-create"),
    path("warehouse/", views.warehouse_view, name="warehouse"),
]