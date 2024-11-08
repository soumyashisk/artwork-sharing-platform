from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.ArtworkListView.as_view(), name="home"),
    path("<int:pk>", views.ArtworkDetailView.as_view(), name="detail"),
    path("add", views.ArtworkCreateView.as_view(), name="create"),
    path("like", views.LikeView, name="like")
]