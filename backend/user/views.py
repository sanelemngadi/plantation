from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages

from user.models import PlantationUser

def is_staff(user):
    return not user.is_staff and not user.is_superuser

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirect to a success page
            return redirect("main:main")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def register_view(request):
    as_admin = request.GET.get("as_admin")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            # Redirect to a success page or login the user
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, "as_admin": as_admin})


def logout_view(request):
    logout(request)
    return redirect("login")

def settings_view(request):
    return render(request, "settings.html")


@user_passes_test(is_staff)
def admin_key_view(request):
    if request.method == "POST":
        data = request.POST.get("admin_key")

        print(data)

        # user = PlantationUser.objects.filter(pk = request.pk)
        # if not user:
            # you need to confirm your email first
            # pass

        request.user.is_admin = True
        request.user.is_superuser = True
        request.user.is_staff = True
        request.user.save()
        # user.update(is_admin = True)
        # user.update(is_superuser = True)

        messages.success(request, 'Username updated successfully.')
    return render(request, "set-admin-key.html")