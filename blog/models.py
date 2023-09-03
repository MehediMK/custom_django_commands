from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    slug = models.SlugField(max_length=100, null=True)
    url = models.URLField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=1000, blank=True)
    post_image_url = models.URLField(max_length=200, null=True)
    post_thumbnail_url = models.URLField(max_length=200, null=True)
    status = models.CharField(max_length=20, null=False)
    category = models.CharField(max_length=20, null=False)
    published_at = models.DateTimeField(null=True, auto_now_add=True)
    updatedAt = models.DateTimeField(null=True, auto_now=True)

    def __str__(self) -> str:
        return self.title


