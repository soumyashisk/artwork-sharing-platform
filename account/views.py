from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Profile

def signup(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        # else:
        #     return render(req, "account/signup.html", context={"form": UserCreationForm, "erros": form.errors})
    else:
        form = UserCreationForm()
    return render(req, "account/signup.html", context={"form": form})


class ProfileDetailView(DetailView):
    context_object_name = "profile"
    template_name = "account/profile.html"

    def get_object(self):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        return Profile.objects.get(user=user)
