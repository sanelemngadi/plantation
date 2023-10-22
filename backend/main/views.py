from django.shortcuts import render, get_object_or_404, redirect
from main.models import PlantationService, PlantationProduct
from main.forms import PlantationProductForm, PlantationServiceForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    services = PlantationService.objects.all()
    return render(request, "main.html", { 
        "services": services
    })


def service_list_view(request, pk):
    print(pk)
    service = get_object_or_404(PlantationService, pk = pk)
    return render(request, "service.detail.html", { "service": service })

def product_list_view(request):
    products = PlantationProduct.objects.all() # we need to keep track of who created the product
    return render(request, "product-list.html", { "products": products })

@login_required(login_url='/users/login/')
def product_detail_view(request, pk):
    product = get_object_or_404(PlantationProduct, pk = pk)
    similar = PlantationProduct.objects.filter(service__pk = product.service.pk).exclude(pk = pk)[:3]
    return render(request, "product.detail.html", { "product": product, "similar": similar })

@login_required(login_url='/users/login/')
def product_create_view(request, pk):
    form = PlantationProductForm()

    service = get_object_or_404(PlantationService, pk = pk)
    if request.method == "POST":
        form = PlantationProductForm(request.POST)

        if form.is_valid():
            product = form.save(False)
            product.service = service
            product.save()
            print("item is saved")
            return redirect("main:service-detail", service.pk)
    return render(request, "create-product.html", {"form": form, "service": service })

@login_required(login_url='/users/login/')
def service_create_view(request):
    form = PlantationServiceForm()

    if request.method == "POST":
        form = PlantationServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:main")

    return render(request, "create-service.html", {"form": form})
