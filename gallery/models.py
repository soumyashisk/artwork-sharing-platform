from django.db import models
from django.urls import reverse


# Create your models here.
class Artwork(models.Model):
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to="artworks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery:detail", kwargs={"pk": self.pk})
