from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.ArtworkListView.as_view(), name="home"),
    path("<int:pk>", views.ArtworkDetailView.as_view(), name="detail"),
    path("add", views.ArtworkCreateView.as_view(), name="create"),
    path("like", views.LikeView, name="like"),
    path("<int:pk>/delete", views.ArtworkDeleteView.as_view(), name="delete"),
    path("manage", views.ArtworkListView.as_view(view_mode="created_by_user"), name="manage")
    # path("<int:pk>", views.ArtworkDetailView.as_view(context_object_name = "artworks"), name="manage")
]