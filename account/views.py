from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = UserCreationForm()
    return render(req, "account/signup.html", context={"form": UserCreationForm})
