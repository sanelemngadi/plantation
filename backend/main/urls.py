from django.urls import path
# from main.views import ( index, service_list_view, product_detail_view, 
#                         product_list_view, product_create_view, service_create_view)

from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="main"),
    # path("services/<int:pk>/", service_list_view, name="service-detail"),
    # path("products/<int:pk>/", product_detail_view, name="product-detail"),
    # path("products/", product_list_view, name="products"),
    # path("product-new/service/<int:pk>/", product_create_view, name="new-product"),
    # path("service-new/", service_create_view, name="new-service"),
]