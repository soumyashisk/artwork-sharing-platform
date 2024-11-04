from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .models import Artwork
from .forms import LikeForm


class ArtworkListView(ListView):
    # model = Artwork
    template_name = "gallery/index.html"
    queryset = Artwork.objects.order_by("-created_at")
    context_object_name = "artworks"


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "gallery/detail.html"
    context_object_name = "artwork"

# @login_required
def Like(req):
    form = LikeForm(req.POST or None)
    if form.is_valid():
        id = req.POST.get("id", None)
        if id is not None:
            artwork = Artwork.objects.get(id=id)
            artwork.likes +=  1
            artwork.save()
            return render(
                req, "gallery/like.html", context={"artwork": Artwork.objects.get(id=id)}
            )
    # else:
    #     return HttpResponse("Method Not Allow")

    return render(
        req, "gallery/like.html", context={"artwork": Artwork.objects.get(id=id)}
    )
