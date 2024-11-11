from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.ArtworkListView.as_view(), name="home"),
    path("<int:pk>", views.ArtworkDetailView.as_view(), name="detail"),
    path("add", views.ArtworkCreateView.as_view(), name="create"),
    path("<int:pk>/edit", views.ArtworkUpdateView.as_view(), name="update"),
    path("like", views.LikeView, name="like"),
    path("<int:pk>/delete", views.ArtworkDeleteView.as_view(), name="delete"),
    path("manage", views.ManageArtworkListView.as_view(), name="manage")
]