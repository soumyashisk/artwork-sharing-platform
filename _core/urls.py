"""
URL configuration for _core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views as account_views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("admin", admin.site.urls),
    path("", include("gallery.urls")),
    path("signup", account_views.signup, name="signup"),
    path("login", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("profile/<str:username>", account_views.ProfileDetailView.as_view(), name="signup"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)