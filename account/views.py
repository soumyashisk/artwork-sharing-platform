from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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
