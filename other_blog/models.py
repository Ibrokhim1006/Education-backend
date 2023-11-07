from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    img = models.ImageField(upload_to="blog/")
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
