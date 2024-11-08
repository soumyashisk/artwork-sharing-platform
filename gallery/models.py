from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Artwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to="artworks")
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery:detail", kwargs={"pk": self.pk})

class Like(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('artwork', 'user')