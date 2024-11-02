from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.ArtworkListView.as_view(), name="home"),
]