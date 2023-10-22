from django.shortcuts import render, redirect, get_object_or_404
from rentals.forms import PlantationRentalForm
from rentals.models import PlantationRentalModel
from django.contrib.auth.decorators import login_required
from main.models import PlantationProduct

# Create your views here.
@login_required(login_url='/users/login/')
def list_view(request):
    return render(request, "rentals.html")

@login_required(login_url='/users/login/')
def confirm_rental_view(request, pk):
    rental = get_object_or_404(PlantationRentalModel, pk = pk)
    return render(request, "confirm-rental.html", { "rental": rental })

@login_required(login_url='/users/login/')
def create_view(request, pk):
    form = PlantationRentalForm()

    rented_product = get_object_or_404(PlantationProduct, pk = pk)

    if request.method == "POST":
        form = PlantationRentalForm(request.POST)

        if form.is_valid():
            instance = form.save(False)
            instance.user  = request.user
            instance.save()

            return redirect("confirm-rental", pk = instance.pk)

    return render(request, "create-rental.html", { "form": form, "product": rented_product })