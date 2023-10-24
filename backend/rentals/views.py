from django.shortcuts import render, redirect, get_object_or_404
from rentals.forms import PlantationRentalForm
from rentals.models import PlantationRentalModel
from django.contrib.auth.decorators import login_required, user_passes_test
from products.models import PlantationProduct
from datetime import date

def is_admin(user):
    return user.is_staff or user.is_superuser


def is_user(user):
    return not user.is_staff or not user.is_superuser


# Create your views here.
@login_required(login_url='/users/login/')
def rental_list_view(request):
    rentals = PlantationRentalModel.objects.filter(user = request.user)

    if is_admin(request.user):
        rentals = PlantationRentalModel.objects.all()

    count_unread = rentals.filter(viewed = False).count() 
    count_not_accepted = rentals.filter(accepted = False).count() 
    total = rentals.count()

    # if total == count_not_accepted:
    #     count_not_accepted = "all"

    context = { 
        "rentals": rentals, 
        "count_unread": count_unread,
        "count_not_accepted": count_not_accepted,
        "total": total
        }
    return render(request, "rentals.html", context)

@login_required(login_url='/users/login/')
def confirm_rental_view(request, pk):
    rental = get_object_or_404(PlantationRentalModel, pk = pk)

    return render(request, "confirm-rental.html", { "rental": rental })

@login_required(login_url='/users/login/')
def rental_create_view(request, pk):
    form = PlantationRentalForm()

    rented_product = get_object_or_404(PlantationProduct, pk = pk)

    if request.method == "POST":
        form = PlantationRentalForm(request.POST)

        print("hello world")

        if form.is_valid():
            instance = form.save(False)
            instance.product = rented_product
            instance.user = request.user

            if instance.date_from <= date.today():
                print("this have to be after today")
                # raise ValueError("invalid items")
                form.add_error("date_from","Date from must always bigger than today")
                return render(request, "create-rental.html", { "form": form, "product": rented_product })

            if instance.date_from > instance.date_to:
                form.add_error("date_from","Date to must always bigger than date from")
                return render(request, "create-rental.html", { "form": form, "product": rented_product })

            if instance.date_from == instance.date_to:
                form.add_error("date_from","The item cannot be borrowed and returned same day")
                return render(request, "create-rental.html", { "form": form, "product": rented_product })
            instance.save()

            return redirect("confirm-rental", pk = instance.pk)

    return render(request, "create-rental.html", { "form": form, "product": rented_product })

@user_passes_test(is_admin)
def admin_rentals_view(request):
    pass


user_passes_test(is_user)
def user_rentals_view(request):
    pass

def rental_detail_view(request, pk):
    rental = get_object_or_404(PlantationRentalModel, pk = pk)

    if rental:
        rental.viewed = True
        rental.save()

    return render(request, "rental-admin-detail.html", { "rental": rental})


def accept_rental(request, pk, accept):
    rental = get_object_or_404(PlantationRentalModel, pk = pk)

    if rental:
        if accept == "yes":
            rental.accepted = True
            rental.save()

    return redirect("rental-detail", pk)