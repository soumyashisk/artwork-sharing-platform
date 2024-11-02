# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Artwork
class ArtworkListView(ListView):
    model = Artwork
    template_name = "gallery/index.html"
    context_object_name = "artworks"


# Create your views here.
# def index(req):
#     return render(
#         req,
#         "gallery/index.html",
#         context={"item": map(lambda a: a * 200, range(1, 11))},
#     )
