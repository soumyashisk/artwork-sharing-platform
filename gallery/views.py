from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Artwork, Like
from .forms import LikeForm


class ArtworkListView(ListView):
    template_name = "gallery/index.html"
    context_object_name = "artworks"
    queryset = Artwork.objects.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user = self.request.user

            liked_artwork_ids = set(
                Like.objects.filter(user=user).values_list("artwork_id", flat=True)
            )

            for artwork in context["artworks"]:
                artwork.liked = artwork.id in liked_artwork_ids

        return context


class ManageArtworkListView(LoginRequiredMixin, ListView):
    template_name = "gallery/manage.html"
    context_object_name = "artworks"

    def get_queryset(self):
        return Artwork.objects.filter(user=self.request.user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        liked_artwork_ids = set(
            Like.objects.filter(user=user).values_list("artwork_id", flat=True)
        )

        for artwork in context["artworks"]:
            artwork.liked = artwork.id in liked_artwork_ids

        return context


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "gallery/detail.html"
    context_object_name = "artwork"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context["artwork"].liked = Like.objects.filter(
                user=self.request.user, artwork=context["artwork"]
            ).exists()
        else:
            context["artwork"].liked = False

        return context


class ArtworkCreateView(LoginRequiredMixin, CreateView):
    model = Artwork
    fields = ["title", "desc", "image"]
    template_name = "gallery/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data provided.")
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Artwork Added Successfully!")
        return self.object.get_absolute_url()


class ArtworkUpdateView(LoginRequiredMixin, UpdateView):
    model = Artwork
    fields = ["title", "desc", "image"]
    template_name = "gallery/update.html"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data provided.")
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Artwork Edited Successfully!")
        return self.object.get_absolute_url()


# TODO: Add delte confirmation
class ArtworkDeleteView(LoginRequiredMixin, DeleteView):
    model = Artwork
    template_name = "gallery/confirm-delete.html"
    success_url = reverse_lazy("gallery:manage")

    def dispatch(self, request, *args, **kwargs):
        artwork = self.get_object()
        if artwork.user != request.user and not request.user.is_superuser:
            return redirect(reverse_lazy("login"))

        return super().dispatch(request, *args, **kwargs)


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
