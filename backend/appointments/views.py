from django.shortcuts import render, get_object_or_404, redirect
from appointments.forms import PlantationAppointmentForm
from appointments.models import PlantationAppointmentsModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login/')
def appointment_list_view(request):
    appointments = PlantationAppointmentsModel.objects.all().filter(user = request.user)

    if request.user.is_staff or request.user.is_superuser:
        appointments = PlantationAppointmentsModel.objects.all()
        
    return render(request, "appointments.html", { "appointments": appointments })

@login_required(login_url='/users/login/')
def appointment_confirm_view(request, pk):
    appointment = get_object_or_404(PlantationAppointmentsModel, pk=pk)
    return render(request, "confirm-appointment.html", { "appointment": appointment})
    
@login_required(login_url='/users/login/')
def appointment_create_view(request):
    form = PlantationAppointmentForm()
    appointment = PlantationAppointmentsModel.objects.all().first()

    if appointment:
        if not appointment.confirmed:
            return redirect("confirm-appointment", pk = appointment.pk)

    if request.method == "POST":
        form = PlantationAppointmentForm(request.POST)
        if appointment:
            return redirect("appointments")
        
        if form.is_valid():
            appointment = form.save(False)
            appointment.user = request.user
            appointment.save()

            return redirect("confirm-appointment", pk = appointment.pk)

    return render(request, "create-appointment.html", { "form": form })

def appointment_detail_view(request, pk):
    appointment = get_object_or_404(PlantationAppointmentsModel, pk = pk)
    return render(request, "detail-appointment.html", { "appointment": appointment })