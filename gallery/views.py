from django.shortcuts import render


# Create your views here.
def index(req):
    return render(
        req,
        "gallery/index.html",
        context={"item": map(lambda a: a * 200, range(1, 11))},
    )
