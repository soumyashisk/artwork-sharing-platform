from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  image = models.ImageField(upload_to="uploads/profile_pics/")
  artist_name = models.CharField(max_length=100)
  bio = models.TextField(max_length=255, default="Hello, I am an artist.")
  
  def __str__(self):
    return self.user.username

  def get_absolute_url(self):
    return reverse("account:profile", kwargs={"username": self.user.username})