# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Artwork
class ArtworkListView(ListView):
    model = Artwork
    template_name = "gallery/index.html"
    context_object_name = "artworks"

class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "gallery/detail.html"
    context_object_name = "artwork"