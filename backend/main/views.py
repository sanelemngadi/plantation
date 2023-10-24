from django.shortcuts import render, get_object_or_404, redirect
from services.models import PlantationService
# from main.forms import PlantationProductForm, PlantationServiceForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    services = PlantationService.objects.all()
    return render(request, "main.html", { 
        "services": services
    })

