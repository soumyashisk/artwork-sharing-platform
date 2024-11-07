from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_POST
from .models import Artwork, Like
from .forms import LikeForm


class ArtworkListView(ListView):
    # model = Artwork
    template_name = "gallery/index.html"
    queryset = Artwork.objects.order_by("-created_at")
    context_object_name = "artworks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = self.request.user
            
            liked_artwork_ids = set(Like.objects.filter(user=user).values_list('artwork_id', flat=True))
            print(liked_artwork_ids)
        
            for artwork in context['artworks']:
                artwork.liked = artwork.id in liked_artwork_ids
        
        return context


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "gallery/detail.html"
    context_object_name = "artwork"

# ISSUE: No dislike handling
@require_POST
def LikeView(req):
    form = LikeForm(req.POST or None)
    if form.is_valid():
        id = req.POST.get("id", None)
        if req.user.is_authenticated and id is not None:
            artwork = Artwork.objects.get(id=id)
            like = Like(artwork=artwork, user=req.user)
            like.save()
            artwork.likes += 1
            artwork.save()
    return render(
        req,
        "gallery/like.html",
        context={"artwork": Artwork.objects.get(id=id)},
    )
