from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.http import HttpResponse
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from xhtml2pdf import pisa
from django.template.loader import get_template

from orders.models import PlantationOrderModel
from orders.forms import PlantationOrderForm

# import weasyprint

# from payfast.forms import PayFastForm

# Create your views here.
@login_required(login_url='/users/login/')
def order_list_view(request):
    orders = PlantationOrderModel.objects.all()
    return render(request, "orders.html", { "orders": orders })

@login_required(login_url='/users/login/')
def order_create_view(request):
    form = PlantationOrderForm()

    if request.method == "POST":
        form = PlantationOrderForm(request.POST)
        if form.is_valid():
            order = form.save(False)
            order.user = request.user
            order.save()
            return redirect("orders")

    return render(request, "create-order.html", { "form": form })

# @login_required(login_url='/users/login/')
# def create_view(request):
#     pass

def invoice_view(request):
    # Load your HTML content from a template file
    # template = get_template('main.html')
    # html = template.render()

    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="example.pdf"'

    # Create a PDF object, using the response object as its "file."
    # pisa_status = pisa.CreatePDF(html, dest=response)
    # if pisa_status.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')

    # return response
    return render(request, "invoice.html")

# def initiate_payment(request):
#     form = PayFastForm(initial={
#         "merchant_id": settings.PAYFAST_MERCHANT_ID,
#         "merchant_key": settings.PAYFAST_MERCHANT_KEY,
#         "amount": 100.00,  # Set your desired payment amount
#         # Add other form fields as needed
#     })
#     return render(request, 'payfast.html', {'form': form})


def download_invoice_view(request):
    # Load your HTML content from a template file
    # template = get_template('invoice.html')
    # html = template.render()

    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="example.pdf"'

    # #Create a PDF object, using the response object as its "file."
    # pisa_status = pisa.CreatePDF(html, dest=response)
    # if pisa_status.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'

    html = render(request, 'invoice.html').content

    # pisa_status = pisa.CreatePDF(html, dest=response)

    # if pisa_status.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

def page_invoice_view(request, pk):
    order = get_object_or_404(PlantationOrderModel, pk=pk)
    return render(request, "invoice-home.html", { "order": order })