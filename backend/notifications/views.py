from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from events.models import PlantationEventModel

# Create your views here.
def is_stuff(user):
    return user and (not user.is_superuser or not user.is_staff)

@user_passes_test(is_stuff)
def notification_list_view(request):
    events = PlantationEventModel.objects.all()
    return render(request, "notifications.html", { "events": events })