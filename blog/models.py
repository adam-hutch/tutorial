from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique = True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quick_description = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    img_url = models.CharField(max_length=1000,  unique=True)