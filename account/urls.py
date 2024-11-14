from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "account"
urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("profile/<str:username>", views.ProfileDetailView.as_view(), name="profile"),
    path(
        "profile/<str:username>/edit",
        views.ProfileUpdateView.as_view(),
        name="edit_profile",
    ),
]
