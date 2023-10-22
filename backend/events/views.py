from django.shortcuts import render, redirect
from events.forms import PlantationEventForm
from events.models import PlantationEventModel
from django.contrib.auth.decorators import login_required, user_passes_test

def is_stuff(user):
    return user.is_superuser or user.is_staff

# Create your views here.
@login_required(login_url='/users/login/')
@user_passes_test(is_stuff)
def list_view(request):
    events = PlantationEventModel.objects.all()
    return render(request, "events.html", { "events": events })

@login_required(login_url='/users/login/')
@user_passes_test(is_stuff)
def create_view(request):
    form = PlantationEventForm()
    if request.method == "POST":
        form = PlantationEventForm(request.POST)

        if form.is_valid():
            event = form.save(False)
            # form_sent = True
            event.host = request.user
            event.save()
            return redirect("events")
    return render(request, "create-events.html", {"form": form})