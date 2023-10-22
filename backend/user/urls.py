from django.urls import path
from user.views import login_view, register_view, logout_view, settings_view, admin_key_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("settings/", settings_view, name="settings"),
    path("administration-request/", admin_key_view, name="admin-key"),
]