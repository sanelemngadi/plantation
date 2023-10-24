from django.shortcuts import render, redirect, get_object_or_404
from suppliers.models import PlantationSupplier
from suppliers.forms import PlantationSupplierCreateForm

# Create your views here.
def supplier_list_view(request):
    suppliers = PlantationSupplier.objects.all()
    return render(request, "suppliers.html", { "suppliers": suppliers } )

def supplier_remove_view(request, pk):
    supplier = get_object_or_404(PlantationSupplier, pk = pk)

    if request.method == "POST" and supplier:
        supplier.delete()
        return redirect("suppliers")
    
    return render(request, "supplier-remove.html", { "supplier": supplier } )

def supplier_update_view(request, pk):
    supplier = get_object_or_404(PlantationSupplier, pk = pk)
    form = PlantationSupplierCreateForm(instance=supplier)

    if request.method == "POST" and supplier:
        form = PlantationSupplierCreateForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect("suppliers")
        
    return render(request, "supplier-update.html", { "supplier": supplier , "form": form } )

def supplier_create_view(request):
    form = PlantationSupplierCreateForm()

    if request.method == "POST":
        form = PlantationSupplierCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("suppliers")
        
    return render(request, "supplier-create.html", { "form": form })