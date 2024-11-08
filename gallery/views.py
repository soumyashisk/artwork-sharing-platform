from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Artwork, Like
from .forms import LikeForm


class ArtworkListView(ListView):
    template_name = "gallery/index.html"
    queryset = Artwork.objects.order_by("-created_at")
    context_object_name = "artworks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user = self.request.user

            liked_artwork_ids = set(
                Like.objects.filter(user=user).values_list("artwork_id", flat=True)
            )
            print(liked_artwork_ids)

            for artwork in context["artworks"]:
                artwork.liked = artwork.id in liked_artwork_ids

        return context


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "gallery/detail.html"
    context_object_name = "artwork"


class ArtworkCreateView(LoginRequiredMixin, CreateView):
    model = Artwork
    fields = ["title", "desc", "image"]
    template_name = "gallery/artwork-form.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

@require_POST
def LikeView(req):
    form = LikeForm(req.POST or None)
    if form.is_valid():
        id = req.POST.get("id", None)
        if id is not None:
            try:
                artwork = Artwork.objects.get(id=id)
            except Artwork.DoesNotExist:
                return HttpResponse(status=404)

            artwork.liked = False
            if req.user.is_authenticated:
                like, created = Like.objects.get_or_create(
                    user=req.user, artwork=artwork
                )

                if created:
                    artwork.likes += 1
                    artwork.liked = True
                else:
                    like.delete()
                    artwork.likes -= 1
                    artwork.liked = False

                artwork.save()
            else:
                messages.warning(req, "Please log in to like posts.")

            return render(
                req,
                "gallery/like.html",
                context={"artwork": artwork},
            )

        else:
            return HttpResponse(status=404)
