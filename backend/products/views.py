from django.shortcuts import render, get_object_or_404, redirect
from products.models import PlantationProduct
from products.forms import PlantationProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from services.models import PlantationService
# Create your views here.

def is_admin(user):
    return user.is_staff or user.is_superuser

def product_list_view(request):
    products = PlantationProduct.objects.all() # we need to keep track of who created the product
    return render(request, "product-list.html", { "products": products })

# @login_required(login_url='/users/login/')
def product_detail_view(request, pk):
    product = get_object_or_404(PlantationProduct, pk = pk)
    similar = PlantationProduct.objects.filter(service__pk = product.service.pk).exclude(pk = pk)[:3]
    return render(request, "product-detail.html", { "product": product, "similar": similar })

@login_required(login_url='/users/login/')
def product_create_view(request, pk):
    form = PlantationProductForm()

    service = get_object_or_404(PlantationService, pk = pk)
    if request.method == "POST":
        form = PlantationProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(False)
            product.service = service
            product.save()
            print("item is saved")
            return redirect("service-detail", service.pk)
    return render(request, "product-create.html", {"form": form, "service": service })

@user_passes_test(is_admin)
def product_remove_view(request, pk):
    return render(request, "product-remove.html")

@user_passes_test(is_admin)
def product_update_view(request, pk):
    return render(request, "product-update.html")