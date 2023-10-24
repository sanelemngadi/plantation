from django.urls import path
from services import views

urlpatterns = [
    path("", views.service_list_view, name="service-list"),
    path("service/<int:pk>/", views.service_detail_view, name="service-detail"),
    path("service-remove/<int:pk>/", views.service_remove_view, name="service-remove"),
    path("service-update/<int:pk>/", views.service_update_view, name="service-update"),
    path("service-create/", views.service_create_view, name="service-create"),
]