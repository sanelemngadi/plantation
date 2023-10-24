from django.shortcuts import render, redirect
from suppliers.forms import PlantationStockingForm
from inventory.forms import PlantationShelfForm, PlantationRowForm, PlantationWareHouseForm
from inventory.models import PlantationWareHouse
from products.models import PlantationProduct
from suppliers.models import PlantationProductInfo
# Create your views here.
def inventory_view(request):
    form = PlantationStockingForm()

    infos = PlantationProductInfo.objects.all()

    products = PlantationProduct.objects.all()
    if request.method == "POST":
        form = PlantationStockingForm(request.POST)
        if form.is_valid():
            stock = form.save(False)
            product = PlantationProduct.objects.filter(pk = stock.product.pk).first()
            if product:
                product.stock = stock.items_recieved
                product.save()
            
            stock.save()
            return redirect("main:main")
            

    return render(request, "inventory.html", { "form": form, "products": products, "infos": infos })

def row_create_view(request):
    form = PlantationRowForm()

    if request.method == "POST":
        form = PlantationRowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("shelf-create")

    return render(request, "row-create.html", { "form": form})


def shelf_create_view(request):
    form = PlantationShelfForm()

    if request.method == "POST":
        form = PlantationShelfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("row-create")

    return render(request, "shelf-create.html", { "form": form })

def warehouse_view(request):
    form = PlantationWareHouseForm()

    warehouse = PlantationWareHouse.objects.first()
    if warehouse:
        form = PlantationWareHouseForm(instance=warehouse)
        if form.is_valid():
            form.save()
            return render(request, "warehouse.html", { "form": form })
        
    if request.method == "POST":
        form = PlantationWareHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("row-create")

    return render(request, "warehouse.html", { "form": form })


