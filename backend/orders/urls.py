from django.urls import path
from orders.views import order_create_view, order_list_view, invoice_view, download_invoice_view
# initiate_payment

urlpatterns = [
    path("", order_list_view, name="orders"),
    path("create-new/", order_create_view, name="new-order"),
    path("invoice/", invoice_view, name="invoice"),
    path("download-invoice/", download_invoice_view, name="download-invoice"),
]