from django.shortcuts import render, get_object_or_404, redirect
from services.models import PlantationService
# PlantationProduct
from services.forms import PlantationServiceForm
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def service_list_view(request):
    services = PlantationService.objects.all()
    return render(request, "service-list.html", { "services": services })

def service_detail_view(request, pk):
    service = get_object_or_404(PlantationService, pk = pk)
    # similar = PlantationService.objects.filter(service__pk = product.service.pk).exclude(pk = pk)[:3]
    return render(request, "service-detail.html", { "service": service })

@login_required(login_url='/users/login/')
def service_create_view(request):
    form = PlantationServiceForm()

    if request.method == "POST":
        form = PlantationServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:main")

    return render(request, "service-create.html", {"form": form})

@user_passes_test(is_admin)
def service_remove_view(request, pk):
    return render(request, "service-remove.html")

@user_passes_test(is_admin)
def service_update_view(request, pk):
    return render(request, "service-update.html")
